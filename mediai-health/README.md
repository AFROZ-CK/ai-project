# 🏥 MediAI – Intelligent Health Assistant

A full-stack AI-powered health assistant that helps users understand symptoms, get preliminary health guidance, track medications, and find nearby doctors. Built with React, Flask, and Google Gemini.

> ⚠️ **Disclaimer**: MediAI is for informational purposes only and does not replace professional medical advice. Always consult a qualified healthcare provider for medical decisions.

## 🚀 Features

- **Symptom Checker** – AI analyzes symptoms and suggests possible conditions
- **Drug Interaction Checker** – Check safety of medication combinations
- **Health Q&A Chat** – Natural language medical queries powered by Gemini
- **Medication Reminders** – Smart reminder system with dosage tracking
- **Doctor Finder** – Nearby specialist recommendations based on symptoms
- **Health Analytics Dashboard** – Track vitals, weight, and health metrics over time
- **Emergency Guidance** – Immediate steps for common medical emergencies

## 🏗️ Tech Stack

### Frontend
- **React 18** + TypeScript
- **Tailwind CSS** + Ant Design
- **Recharts** for health data visualization
- **Service Workers** for offline capability + PWA

### Backend
- **Flask** + Python 3.11
- **Google Gemini Pro** API
- **PostgreSQL** for user health data
- **Redis** for session management
- **FHIR** (HL7 Fast Healthcare Interoperability) compliant data models

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/symptoms/analyze` | AI symptom analysis |
| POST | `/api/chat` | Health Q&A chat |
| POST | `/api/drugs/interactions` | Check drug interactions |
| GET | `/api/doctors/nearby` | Find nearby specialists |
| GET | `/api/health/records` | User health records |
| POST | `/api/medications/reminder` | Set medication reminder |

## 📊 AI Models Used

- **Google Gemini Pro** – Medical Q&A and symptom analysis
- **Custom NER model** – Medical entity recognition (symptoms, drugs, conditions)
- **Classifier** – Urgency triage (routine / urgent / emergency)

## 🔐 Privacy & Security

- End-to-end encryption for all health data
- HIPAA-compliant data storage practices
- Zero-retention policy for chat conversations
- OAuth 2.0 authentication

## 📄 License

MIT


<!-- 2026-11-22T14:35:00 -->

<!-- 2026-07-06T14:34:00 -->

<!-- 2026-10-11T19:36:00 -->

<!-- 2026-07-16T22:07:00 -->

<!-- 2026-06-25T11:45:00 -->

<!-- 2026-09-10T10:03:00 -->

<!-- 2026-06-13T10:46:00 -->

<!-- 2026-09-10T20:48:00 -->

<!-- 2026-11-05T13:40:00 -->

<!-- 2026-08-06T14:11:00 -->

<!-- 2026-10-03T09:00:00 -->

<!-- 2026-08-16T11:22:00 -->

<!-- 2026-11-15T12:14:00 -->

<!-- 2026-10-12T11:10:00 -->
