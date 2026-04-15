import OpenAI from 'openai';
import { Readable } from 'stream';

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

export interface InterviewQuestion {
  id: string;
  text: string;
  type: 'behavioral' | 'technical' | 'situational';
  difficulty: 'easy' | 'medium' | 'hard';
  hints: string[];
  idealAnswer?: string;
}

export interface AnswerAnalysis {
  score: number; // 0-100
  contentScore: number;
  clarityScore: number;
  structureScore: number;
  strengths: string[];
  improvements: string[];
  betterAnswer: string;
  keywords: string[];
  starStructure: {
    situation: boolean;
    task: boolean;
    action: boolean;
    result: boolean;
  };
}

export class InterviewAIService {
  
  async generateQuestions(role: string, difficulty: string, count: number = 10): Promise<InterviewQuestion[]> {
    const prompt = `Generate ${count} interview questions for a ${role} position at ${difficulty} level.
    
    Include a mix of:
    - 40% Behavioral questions (STAR method expected)
    - 40% Technical questions specific to ${role}
    - 20% Situational / problem-solving questions
    
    For each question provide:
    - Unique ID
    - Question text
    - Type (behavioral/technical/situational)
    - 2-3 hints to guide the candidate
    
    Return as JSON array matching the InterviewQuestion schema.`;

    const response = await openai.chat.completions.create({
      model: 'gpt-4-turbo-preview',
      messages: [{ role: 'user', content: prompt }],
      response_format: { type: 'json_object' },
      temperature: 0.8
    });

    const result = JSON.parse(response.choices[0].message.content!);
    return result.questions;
  }

  async analyzeAnswer(
    question: string,
    transcript: string,
    role: string
  ): Promise<AnswerAnalysis> {
    const prompt = `You are an expert interviewer for ${role} positions. Analyze this interview answer.

    Question: "${question}"
    Candidate's Answer: "${transcript}"
    
    Evaluate on:
    1. Content Accuracy & Relevance (0-100)
    2. Communication Clarity (0-100)
    3. Answer Structure - especially STAR for behavioral questions (0-100)
    4. Identify specific strengths (what they did well)
    5. Specific improvements with examples
    6. Write a better sample answer
    7. Keywords they should have mentioned
    8. STAR structure presence (true/false for each component)
    
    Overall score = weighted average of above scores.
    
    Return as JSON matching AnswerAnalysis interface.`;

    const response = await openai.chat.completions.create({
      model: 'gpt-4-turbo-preview',
      messages: [{ role: 'user', content: prompt }],
      response_format: { type: 'json_object' },
      temperature: 0.5
    });

    return JSON.parse(response.choices[0].message.content!) as AnswerAnalysis;
  }

  async transcribeAudio(audioBuffer: Buffer, filename: string): Promise<string> {
    const file = new File([audioBuffer], filename, { type: 'audio/webm' });
    
    const transcription = await openai.audio.transcriptions.create({
      file,
      model: 'whisper-1',
      language: 'en',
      response_format: 'text'
    });
    
    return transcription;
  }

  async generateFollowUpQuestion(
    originalQuestion: string,
    answer: string,
    role: string
  ): Promise<string> {
    const prompt = `Based on this interview exchange, generate a natural follow-up question.
    
    Original Question: "${originalQuestion}"
    Candidate's Answer: "${answer}"
    Role: ${role}
    
    The follow-up should dig deeper into an interesting aspect of their answer.
    Return only the question text.`;

    const response = await openai.chat.completions.create({
      model: 'gpt-4-turbo-preview',
      messages: [{ role: 'user', content: prompt }],
      max_tokens: 150,
      temperature: 0.7
    });

    return response.choices[0].message.content!.trim();
  }

  async generateSessionSummary(
    answers: Array<{ question: string; analysis: AnswerAnalysis }>
  ): Promise<{
    overallScore: number;
    topStrengths: string[];
    priorityImprovements: string[];
    readinessLevel: string;
    studyPlan: string[];
  }> {
    const avgScore = answers.reduce((sum, a) => sum + a.analysis.score, 0) / answers.length;
    
    const analysisData = answers.map(a => ({
      question: a.question,
      score: a.analysis.score,
      strengths: a.analysis.strengths,
      improvements: a.analysis.improvements
    }));

    const prompt = `Summarize this complete interview session and create a study plan.
    
    Overall Average Score: ${avgScore}
    Session Data: ${JSON.stringify(analysisData)}
    
    Return JSON with:
    - overallScore: number
    - topStrengths: string[] (3 key strengths shown across session)
    - priorityImprovements: string[] (3 most important things to improve)
    - readinessLevel: "Not Ready" | "Almost Ready" | "Interview Ready" | "Excellent"
    - studyPlan: string[] (5 specific action items to improve before next interview)`;

    const response = await openai.chat.completions.create({
      model: 'gpt-4-turbo-preview',
      messages: [{ role: 'user', content: prompt }],
      response_format: { type: 'json_object' }
    });

    return JSON.parse(response.choices[0].message.content!);
  }
}

// Updated: 2026-09-18T16:55:00

// Updated: 2026-07-13T19:00:00

// Updated: 2026-10-25T11:40:00

// Updated: 2026-09-19T09:00:00

// Updated: 2026-05-10T19:07:00

// Updated: 2026-10-19T21:36:00

// Updated: 2026-11-03T15:36:00

// Updated: 2026-07-15T18:16:00

// Updated: 2026-09-01T15:26:00

// 2026-05-21 09:30

// 2026-05-22 10:00

// 2026-05-26 09:30

// 2026-05-27 10:00

// 2026-05-30 10:30

// 2026-06-04 10:00

// 2026-06-05 11:00

// 2026-06-12 10:00

// 2026-06-16 10:30
