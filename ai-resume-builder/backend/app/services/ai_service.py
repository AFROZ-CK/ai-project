import openai
from typing import Optional
import json
import os
from app.models.resume import ResumeData


class AIResumeService:
    def __init__(self):
        self.client = openai.AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = "gpt-4-turbo-preview"

    async def generate_summary(self, experience: list, skills: list, target_role: str) -> str:
        """Generate a professional summary using GPT-4."""
        prompt = f"""
        You are an expert resume writer. Create a compelling professional summary for a candidate.
        
        Target Role: {target_role}
        Experience: {json.dumps(experience)}
        Skills: {', '.join(skills)}
        
        Write a 3-4 sentence professional summary that:
        1. Highlights key achievements with metrics where possible
        2. Is ATS-optimized with relevant keywords
        3. Shows value proposition clearly
        4. Is written in first person without using "I"
        
        Return only the summary text, no additional formatting.
        """
        
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=300
        )
        return response.choices[0].message.content.strip()

    async def enhance_experience(self, job_title: str, company: str, 
                                  description: str, achievements: list) -> list[str]:
        """Enhance work experience bullet points with strong action verbs and metrics."""
        prompt = f"""
        You are an expert resume writer. Enhance these work experience bullet points.
        
        Role: {job_title} at {company}
        Original Description: {description}
        Achievements: {json.dumps(achievements)}
        
        Create 4-6 strong bullet points that:
        1. Start with powerful action verbs (Led, Engineered, Architected, Implemented, etc.)
        2. Include quantifiable metrics (%, $, time saved, users, scale)
        3. Show impact and results, not just responsibilities
        4. Use industry-relevant keywords
        
        Return as a JSON array of strings.
        """
        
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6,
            max_tokens=500,
            response_format={"type": "json_object"}
        )
        
        result = json.loads(response.choices[0].message.content)
        return result.get("bullets", [])

    async def optimize_for_job(self, resume_data: ResumeData, job_description: str) -> dict:
        """Tailor resume for a specific job description."""
        prompt = f"""
        You are an ATS optimization expert. Analyze this job description and suggest 
        resume optimizations.
        
        Job Description:
        {job_description}
        
        Current Resume Summary:
        {resume_data.summary}
        
        Current Skills:
        {', '.join(resume_data.skills)}
        
        Provide:
        1. Missing keywords to add
        2. Suggested summary rewrite
        3. Skills to highlight/add
        4. ATS score (0-100)
        
        Return as JSON with keys: missing_keywords, optimized_summary, highlighted_skills, ats_score
        """
        
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=800,
            response_format={"type": "json_object"}
        )
        
        return json.loads(response.choices[0].message.content)

    async def generate_cover_letter(self, resume_data: ResumeData, 
                                     job_description: str, company_name: str) -> str:
        """Generate a personalized cover letter."""
        prompt = f"""
        Write a compelling cover letter for this candidate.
        
        Candidate: {resume_data.name}
        Target Company: {company_name}
        Job Description: {job_description}
        Resume Summary: {resume_data.summary}
        Key Skills: {', '.join(resume_data.skills[:10])}
        
        The cover letter should:
        1. Be 3-4 paragraphs, professional but personable
        2. Reference specific aspects of the job/company
        3. Highlight 2-3 most relevant achievements
        4. Have a strong call-to-action closing
        
        Return only the cover letter text.
        """
        
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8,
            max_tokens=600
        )
        return response.choices[0].message.content.strip()

    async def suggest_skills(self, current_skills: list, target_role: str) -> dict:
        """Suggest additional skills based on target role."""
        prompt = f"""
        For a {target_role} position, analyze these current skills and suggest additions.
        
        Current Skills: {', '.join(current_skills)}
        
        Return JSON with:
        - must_have: Critical missing skills for this role
        - nice_to_have: Beneficial additional skills  
        - trending: Currently trending skills in this field
        """
        
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            response_format={"type": "json_object"}
        )
        return json.loads(response.choices[0].message.content)

# Updated: 2026-08-24T10:36:00

# Updated: 2026-09-12T12:49:00

# Updated: 2026-09-27T12:44:00

# Updated: 2026-06-25T12:39:00

# Updated: 2026-09-04T18:42:00

# Updated: 2026-11-07T13:03:00

# 2026-05-11 11:30

# 2026-05-12 10:00

# 2026-05-12 15:00

# 2026-05-13 09:30

# 2026-06-11 09:00

# 2026-06-16 10:00

# 2026-07-03 10:30

# 2026-07-09 09:30

# 2026-07-21 10:00
