import openai
import ast
import json
import re
from typing import Optional
from dataclasses import dataclass
import os


@dataclass
class ReviewComment:
    line: int
    severity: str  # 'error', 'warning', 'info', 'suggestion'
    category: str  # 'bug', 'security', 'performance', 'style', 'best-practice'
    message: str
    suggestion: Optional[str] = None
    documentation_url: Optional[str] = None


@dataclass
class CodeReview:
    overall_score: int  # 0-100
    summary: str
    comments: list[ReviewComment]
    positive_aspects: list[str]
    priority_fixes: list[str]
    estimated_issues: dict  # counts by severity


class CodeAnalysisService:
    """AI-powered code analysis using GPT-4 and static analysis."""
    
    def __init__(self):
        self.client = openai.AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = "gpt-4-turbo-preview"

    async def review_code(self, code: str, language: str, 
                           focus_areas: list[str] = None) -> CodeReview:
        """Perform comprehensive AI code review."""
        
        focus = focus_areas or ['bugs', 'security', 'performance', 'best-practices', 'readability']
        
        prompt = f"""You are a senior software engineer doing a thorough code review.
        
Language: {language}
Focus Areas: {', '.join(focus)}

Code to Review:
```{language}
{code}
```

Provide a detailed code review including:
1. Overall quality score (0-100)
2. Summary of code quality
3. Line-by-line comments for issues found
4. Positive aspects (what's done well)
5. Top 3 priority fixes

For each issue, specify:
- Line number (approximate if needed)
- Severity: error/warning/info/suggestion
- Category: bug/security/performance/style/best-practice
- Clear explanation
- Specific fix suggestion with code example
- Relevant documentation link if applicable

Return as JSON matching the CodeReview structure:
{{
  "overall_score": 85,
  "summary": "...",
  "comments": [
    {{
      "line": 10,
      "severity": "warning",
      "category": "performance",
      "message": "...",
      "suggestion": "// Fixed code here",
      "documentation_url": "https://..."
    }}
  ],
  "positive_aspects": ["..."],
  "priority_fixes": ["..."],
  "estimated_issues": {{"errors": 0, "warnings": 2, "info": 3, "suggestions": 1}}
}}"""

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
            temperature=0.3
        )
        
        data = json.loads(response.choices[0].message.content)
        
        comments = [ReviewComment(**c) for c in data.get("comments", [])]
        
        return CodeReview(
            overall_score=data["overall_score"],
            summary=data["summary"],
            comments=comments,
            positive_aspects=data.get("positive_aspects", []),
            priority_fixes=data.get("priority_fixes", []),
            estimated_issues=data.get("estimated_issues", {})
        )

    async def explain_code(self, code: str, language: str, 
                            level: str = "intermediate") -> dict:
        """Explain what code does in plain English."""
        
        prompt = f"""Explain this {language} code for a {level} developer.

```{language}
{code}
```

Provide:
1. High-level summary (1-2 sentences)
2. Step-by-step breakdown of what each part does
3. Key concepts used (with brief explanations)
4. Real-world use case for this code
5. Potential edge cases or limitations

Make it educational and clear. Use analogies where helpful.
Return as JSON: {{
  "summary": "...",
  "breakdown": [{{"lines": "1-5", "explanation": "..."}}],
  "concepts": [{{"name": "...", "explanation": "..."}}],
  "use_case": "...",
  "limitations": ["..."]
}}"""

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
            temperature=0.5
        )
        
        return json.loads(response.choices[0].message.content)

    async def scan_security(self, code: str, language: str) -> dict:
        """Scan for security vulnerabilities (OWASP-based)."""
        
        prompt = f"""You are a cybersecurity expert. Scan this {language} code for security vulnerabilities.

```{language}
{code}
```

Check for OWASP Top 10 and common vulnerabilities:
- SQL Injection
- XSS (Cross-Site Scripting)
- Hardcoded credentials/secrets
- Insecure direct object references
- Security misconfiguration
- Sensitive data exposure
- Broken authentication
- CSRF vulnerabilities
- Using components with known vulnerabilities
- Insufficient logging

Return JSON:
{{
  "risk_level": "low|medium|high|critical",
  "vulnerabilities": [
    {{
      "type": "SQL Injection",
      "owasp_category": "A03:2021",
      "severity": "critical",
      "line": 15,
      "description": "...",
      "code_snippet": "...",
      "fix": "...",
      "cve_reference": "..."
    }}
  ],
  "passed_checks": ["..."],
  "security_score": 75
}}"""

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
            temperature=0.1
        )
        
        return json.loads(response.choices[0].message.content)

    async def generate_documentation(self, code: str, language: str) -> str:
        """Auto-generate documentation for code."""
        
        prompt = f"""Generate comprehensive documentation for this {language} code.

```{language}
{code}
```

Generate:
1. Function/class-level docstrings (JSDoc for JS/TS, Python docstrings, Javadoc for Java)
2. Parameter descriptions with types
3. Return value descriptions
4. Usage examples
5. Any important notes or warnings

Return the original code with documentation added. Only return the documented code."""

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=2000
        )
        
        return response.choices[0].message.content

    async def suggest_refactoring(self, code: str, language: str) -> dict:
        """Suggest modern refactoring patterns."""
        
        prompt = f"""Suggest refactoring improvements for this {language} code.

```{language}
{code}
```

Provide:
1. Refactored version using modern patterns
2. List of changes made and why
3. Design patterns applied
4. Before/after comparison
5. Test cases that should still pass

Return JSON:
{{
  "refactored_code": "...",
  "changes": [{{"change": "...", "reason": "...", "pattern": "..."}}],
  "patterns_applied": ["..."],
  "improvements": ["readability", "performance", "maintainability"]
}}"""

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
            temperature=0.4,
            max_tokens=3000
        )
        
        return json.loads(response.choices[0].message.content)


# Updated: 2026-10-31T18:09:00

# Updated: 2026-07-13T15:51:00

# Updated: 2026-07-22T20:58:00

# Updated: 2026-06-29T10:52:00

# Updated: 2026-08-06T21:05:00

# Updated: 2026-05-11T18:22:00

# Updated: 2026-11-08T09:36:00

# Updated: 2026-09-13T18:11:00

# Updated: 2026-09-22T19:02:00

# Updated: 2026-10-12T13:27:00

# Updated: 2026-09-04T21:53:00

# Updated: 2026-05-18T21:34:00

# Updated: 2026-06-15T19:00:00

# Updated: 2026-05-16T18:05:00

# Updated: 2026-05-17T16:02:00

# Updated: 2026-08-19T14:42:00

# Updated: 2026-08-25T13:31:00

# Updated: 2026-06-06T14:16:00

# Updated: 2026-10-23T21:58:00

# Updated: 2026-06-19T10:32:00

# Updated: 2026-10-03T09:36:00

# Updated: 2026-09-03T16:58:00

# Updated: 2026-11-04T20:39:00

# Updated: 2026-07-16T18:32:00

# Updated: 2026-07-25T21:28:00

# Updated: 2026-08-17T16:23:00

# Updated: 2026-10-25T09:36:00

# Updated: 2026-05-12T10:47:00

# Updated: 2026-11-19T16:06:00

# Updated: 2026-07-26T22:19:00

# Updated: 2026-09-05T13:45:00

# Updated: 2026-11-07T18:34:00

# Updated: 2026-09-24T21:58:00

# Updated: 2026-06-21T12:45:00
