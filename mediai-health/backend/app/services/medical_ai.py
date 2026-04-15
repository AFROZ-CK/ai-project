import google.generativeai as genai
import os
from typing import Optional
import json


class MedicalAIService:
    """AI service using Google Gemini for medical assistance."""
    
    def __init__(self):
        genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
        self.model = genai.GenerativeModel('gemini-pro')
        self.safety_disclaimer = (
            "\n\n⚠️ This information is for educational purposes only. "
            "Please consult a qualified healthcare professional for medical advice, "
            "diagnosis, or treatment."
        )
    
    def analyze_symptoms(self, symptoms: list[str], age: int, 
                          gender: str, duration: str) -> dict:
        """Analyze symptoms and suggest possible conditions."""
        prompt = f"""You are a medical information assistant. A user is describing their symptoms.

Patient Info:
- Age: {age} years old
- Gender: {gender}
- Symptom Duration: {duration}
- Symptoms: {', '.join(symptoms)}

Provide:
1. Possible conditions (3-5) ordered by likelihood, with brief explanations
2. Urgency level: "routine" (can wait), "soon" (within 48h), "urgent" (same day), "emergency" (call 911)
3. Recommended specialist type to see
4. Immediate self-care steps
5. Red flag symptoms to watch for that would increase urgency

IMPORTANT: Always emphasize this is not a diagnosis. Format as JSON:
{{
  "possible_conditions": [
    {{"name": "...", "likelihood": "high/medium/low", "explanation": "..."}}
  ],
  "urgency": "routine|soon|urgent|emergency",
  "urgency_reason": "...",
  "recommended_specialist": "...",
  "self_care_steps": ["..."],
  "red_flags": ["..."],
  "disclaimer": "..."
}}"""

        response = self.model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                temperature=0.1,  # Low temperature for medical info
                response_mime_type="application/json"
            )
        )
        
        result = json.loads(response.text)
        return result

    def check_drug_interactions(self, medications: list[str]) -> dict:
        """Check for drug interactions between medications."""
        if len(medications) < 2:
            return {"error": "Please provide at least 2 medications to check"}
        
        prompt = f"""You are a pharmacology information assistant.
        
Check for interactions between these medications: {', '.join(medications)}

For each significant interaction found, provide:
- Drugs involved
- Severity: "mild", "moderate", "severe", "contraindicated"
- Mechanism of interaction
- Clinical effect
- Recommendation

Also list which medications are generally safe together.

Return as JSON:
{{
  "interactions": [
    {{
      "drugs": ["...", "..."],
      "severity": "...",
      "mechanism": "...",
      "effect": "...",
      "recommendation": "..."
    }}
  ],
  "safe_combinations": ["..."],
  "overall_risk": "low|moderate|high",
  "consult_pharmacist": true|false
}}"""

        response = self.model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(temperature=0.1)
        )
        return json.loads(response.text)

    def answer_health_question(self, question: str, chat_history: list = None) -> str:
        """Answer a general health question with AI."""
        system_context = """You are MediAI, a helpful and empathetic health information assistant.
You provide accurate, evidence-based health information while always:
1. Being empathetic and understanding
2. Recommending professional medical consultation for personal health decisions
3. Not diagnosing conditions
4. Citing when information is uncertain
5. Being culturally sensitive"""

        chat = self.model.start_chat(history=[])
        
        # Add context from previous messages
        if chat_history:
            for msg in chat_history[-10:]:  # Last 10 messages for context
                chat.history.append({
                    "role": msg["role"],
                    "parts": [msg["content"]]
                })
        
        response = chat.send_message(
            f"{system_context}\n\nUser question: {question}",
            generation_config=genai.GenerationConfig(
                temperature=0.4,
                max_output_tokens=800
            )
        )
        
        return response.text + self.safety_disclaimer

    def get_emergency_steps(self, emergency_type: str) -> dict:
        """Get immediate steps for medical emergencies."""
        prompt = f"""Provide clear, numbered emergency first-aid steps for: {emergency_type}
        
Return as JSON:
{{
  "emergency_type": "...",
  "call_emergency": true|false,
  "immediate_steps": ["1. ...", "2. ...", "..."],
  "do_not_do": ["..."],
  "what_to_tell_911": "...",
  "while_waiting": ["..."]
}}

Be clear, concise, actionable. This may save a life."""

        response = self.model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(temperature=0.1)
        )
        return json.loads(response.text)


# Updated: 2026-06-15T15:00:00

# Updated: 2026-05-21T19:57:00

# Updated: 2026-09-16T09:36:00

# Updated: 2026-06-30T14:04:00

# Updated: 2026-05-16T18:03:00

# Updated: 2026-10-02T12:24:00

# Updated: 2026-06-16T22:18:00

# Updated: 2026-06-28T22:28:00

# Updated: 2026-08-09T17:08:00

# Updated: 2026-10-17T21:31:00

# Updated: 2026-05-28T14:25:00

# Updated: 2026-08-20T17:46:00

# Updated: 2026-06-26T22:22:00

# Updated: 2026-09-05T10:41:00

# Updated: 2026-10-10T17:08:00

# Updated: 2026-06-08T16:18:00

# Updated: 2026-10-13T17:30:00

# Updated: 2026-11-10T17:57:00

# Updated: 2026-10-01T18:00:00

# Updated: 2026-08-21T21:41:00

# Updated: 2026-09-11T18:29:00

# Updated: 2026-11-15T21:56:00

# Updated: 2026-10-30T11:34:00

# Updated: 2026-09-13T11:29:00

# Updated: 2026-09-02T20:18:00
