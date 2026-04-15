# 🎤 Smart Interview Coach

An AI-powered interview preparation platform that uses voice recognition and GPT-4 to simulate real interviews, analyze answers, and provide detailed feedback. Built for final-year students and job seekers.

## 🚀 Features

- **AI Mock Interviews** – Role-specific interview questions from GPT-4
- **Voice Recording & Analysis** – Record answers, get transcription via Whisper API
- **Real-time Feedback** – Instant AI analysis of content, clarity, and confidence
- **Body Language Tips** – Camera integration with posture guidance  
- **Industry-Specific Prep** – Questions for Software, Data Science, Product, Finance
- **Progress Tracking** – Track improvement over multiple sessions
- **Answer Library** – Save best answers for future reference
- **STAR Method Coach** – Guides you to structure behavioral answers

## 🏗️ Tech Stack

### Frontend
- **Next.js 14** (App Router) + TypeScript
- **Tailwind CSS** + Radix UI components
- **Web Speech API** + MediaRecorder for voice
- **Zustand** for state management
- **Chart.js** for progress visualization

### Backend
- **Node.js** + **Express** + TypeScript
- **OpenAI GPT-4** + **Whisper API**
- **Socket.io** for real-time communication
- **MongoDB** + Mongoose
- **JWT Authentication**

## 📁 Project Structure

```
smart-interview-coach/
├── frontend/              # Next.js 14 App
│   ├── src/
│   │   ├── app/           # App Router pages
│   │   ├── components/    # UI components
│   │   ├── hooks/         # Custom hooks (useVoiceRecorder, etc.)
│   │   └── store/         # Zustand state
│   └── package.json
├── backend/               # Node.js + Express API
│   ├── routes/
│   ├── services/
│   ├── models/
│   └── server.ts
└── docker-compose.yml
```

## 🛠️ Setup

```bash
# Backend
cd backend
npm install
cp .env.example .env
npm run dev

# Frontend
cd frontend
npm install
npm run dev
```

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/interview/start` | Start a new interview session |
| POST | `/api/interview/answer` | Submit voice answer for analysis |
| GET | `/api/interview/questions` | Get role-specific questions |
| POST | `/api/transcribe` | Transcribe audio with Whisper |
| GET | `/api/progress/:userId` | Get user progress data |
| POST | `/api/feedback/generate` | Generate detailed feedback |

## 🎯 How It Works

1. **Choose your role** – Software Engineer, Data Analyst, Product Manager, etc.
2. **AI generates questions** – GPT-4 creates relevant, difficulty-calibrated questions
3. **Record your answer** – Browser captures audio via MediaRecorder API
4. **Whisper transcribes** – OpenAI Whisper converts speech to text
5. **GPT-4 analyzes** – Evaluates content accuracy, communication clarity, STAR structure
6. **Get feedback** – Detailed score breakdown with specific improvement tips
7. **Track progress** – Visual dashboard shows improvement over sessions

## 📄 License

MIT

<!-- 2026-09-05T20:54:00 -->

<!-- 2026-06-14T13:44:00 -->

<!-- 2026-10-03T19:42:00 -->

<!-- 2026-05-30T20:36:00 -->

<!-- 2026-09-21T18:01:00 -->

<!-- 2026-09-26T17:42:00 -->

<!-- 2026-06-01T12:51:00 -->

<!-- 2026-07-13T21:47:00 -->

<!-- 2026-07-06T20:20:00 -->

<!-- 2026-05-19T16:21:00 -->

<!-- 2026-09-07T09:37:00 -->

<!-- 2026-11-22T16:39:00 -->

<!-- 2026-11-22T12:07:00 -->

<!-- 2026-11-08T10:33:00 -->

<!-- 2026-10-05T16:36:00 -->

<!-- 2026-08-26T14:49:00 -->

<!-- 2026-10-30T18:40:00 -->

<!-- 2026-06-14T18:17:00 -->

<!-- 2026-10-31T20:09:00 -->

<!-- 2026-05-24T22:41:00 -->

<!-- 2026-06-20T13:36:00 -->

<!-- 2026-05-18T16:34:00 -->

<!-- 2026-05-15 14:00 -->
