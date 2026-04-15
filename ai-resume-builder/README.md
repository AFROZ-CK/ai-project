# 🤖 AI Resume Builder

A full-stack AI-powered resume builder that generates professional, ATS-optimized resumes using GPT-4. Built with React, FastAPI, and OpenAI API.

## 🚀 Features

- **AI-Powered Content Generation** – GPT-4 generates tailored resume sections based on your experience
- **ATS Optimization** – Automatically optimizes keywords for Applicant Tracking Systems
- **Multiple Templates** – 10+ professional resume templates
- **Real-time Preview** – Live PDF preview as you edit
- **Job-Specific Tailoring** – Paste a job description and AI rewrites your resume to match
- **Export Options** – Download as PDF, DOCX, or share via link

## 🏗️ Tech Stack

### Frontend
- **React 18** + TypeScript
- **Tailwind CSS** + shadcn/ui
- **React Query** for state management
- **React PDF** for live preview

### Backend
- **FastAPI** (Python)
- **OpenAI GPT-4 API**
- **PostgreSQL** + SQLAlchemy
- **Redis** for caching
- **Celery** for background tasks

### Infrastructure
- **Docker** + Docker Compose
- **AWS S3** for file storage
- **Vercel** (Frontend) + **Railway** (Backend)

## 📁 Project Structure

```
ai-resume-builder/
├── frontend/
│   ├── src/
│   │   ├── components/     # Reusable UI components
│   │   ├── pages/          # Page components
│   │   ├── hooks/          # Custom React hooks
│   │   ├── utils/          # Helper functions
│   │   └── types/          # TypeScript types
│   ├── public/
│   └── package.json
├── backend/
│   ├── app/
│   │   ├── routes/         # API endpoints
│   │   ├── models/         # Database models
│   │   ├── services/       # Business logic
│   │   └── main.py
│   ├── requirements.txt
│   └── Dockerfile
└── docker-compose.yml
```

## 🛠️ Setup & Installation

### Prerequisites
- Node.js 18+
- Python 3.11+
- PostgreSQL
- OpenAI API Key

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env     # Add your API keys
uvicorn app.main:app --reload
```

### Frontend Setup
```bash
cd frontend
npm install
cp .env.example .env.local
npm run dev
```

### Docker Setup
```bash
docker-compose up --build
```

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/resume/generate` | Generate resume content with AI |
| POST | `/api/resume/optimize` | ATS optimize existing resume |
| GET | `/api/resume/{id}` | Get resume by ID |
| PUT | `/api/resume/{id}` | Update resume |
| POST | `/api/resume/{id}/export` | Export as PDF/DOCX |
| POST | `/api/analyze/job` | Analyze job description |

## 📸 Screenshots

> Live Demo: [ai-resume-builder.vercel.app](https://ai-resume-builder.vercel.app)

## 🤝 Contributing

Pull requests are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) first.

## 📄 License

MIT License – see [LICENSE](LICENSE)

<!-- 2026-07-28T11:56:00 -->

<!-- 2026-09-21T20:00:00 -->

<!-- 2026-05-11T18:44:00 -->

<!-- 2026-05-16T15:31:00 -->

<!-- 2026-08-01T09:55:00 -->

<!-- 2026-07-23T14:13:00 -->

<!-- 2026-05-19T15:27:00 -->

<!-- 2026-05-23T15:53:00 -->

<!-- 2026-06-05T20:02:00 -->

<!-- 2026-11-06T21:52:00 -->

<!-- 2026-09-23T13:40:00 -->

<!-- 2026-11-14T18:39:00 -->

<!-- 2026-05-10 11:00 -->

<!-- 2026-06-25 09:00 -->

<!-- 2026-07-18 09:30 -->
