import express from 'express';
import cors from 'cors';
import helmet from 'helmet';
import { createServer } from 'http';
import { Server } from 'socket.io';
import mongoose from 'mongoose';
import dotenv from 'dotenv';

import authRoutes from './routes/auth';
import interviewRoutes from './routes/interview';
import transcribeRoutes from './routes/transcribe';
import progressRoutes from './routes/progress';
import feedbackRoutes from './routes/feedback';
import { errorHandler } from './middleware/errorHandler';
import { rateLimiter } from './middleware/rateLimiter';

dotenv.config();

const app = express();
const httpServer = createServer(app);
const io = new Server(httpServer, {
  cors: {
    origin: process.env.FRONTEND_URL || 'http://localhost:3000',
    credentials: true
  }
});

// Middleware
app.use(helmet());
app.use(cors({ origin: process.env.FRONTEND_URL, credentials: true }));
app.use(express.json({ limit: '50mb' }));
app.use(express.urlencoded({ extended: true }));
app.use(rateLimiter);

// Routes
app.use('/api/auth', authRoutes);
app.use('/api/interview', interviewRoutes);
app.use('/api/transcribe', transcribeRoutes);
app.use('/api/progress', progressRoutes);
app.use('/api/feedback', feedbackRoutes);

// Socket.io for real-time interview
io.on('connection', (socket) => {
  console.log(`Client connected: ${socket.id}`);

  socket.on('interview:start', async (data) => {
    const { userId, role, difficulty } = data;
    socket.join(`interview:${userId}`);
    
    // Send first question
    const question = await generateFirstQuestion(role, difficulty);
    socket.emit('interview:question', { question, questionNumber: 1 });
  });

  socket.on('interview:answer_submitted', async (data) => {
    const { userId, transcript, questionId } = data;
    
    // Stream feedback in real-time
    socket.emit('interview:analyzing', { message: 'Analyzing your answer...' });
    
    const feedback = await analyzeAnswer(transcript, questionId);
    socket.emit('interview:feedback', feedback);
    
    // Send next question
    const nextQuestion = await getNextQuestion(questionId, userId);
    if (nextQuestion) {
      socket.emit('interview:question', nextQuestion);
    } else {
      socket.emit('interview:complete', { message: 'Interview complete!' });
    }
  });

  socket.on('disconnect', () => {
    console.log(`Client disconnected: ${socket.id}`);
  });
});

// Error handling
app.use(errorHandler);

// Database connection
mongoose.connect(process.env.MONGODB_URI!)
  .then(() => console.log('Connected to MongoDB'))
  .catch(err => console.error('MongoDB connection error:', err));

const PORT = process.env.PORT || 5000;
httpServer.listen(PORT, () => {
  console.log(`Smart Interview Coach API running on port ${PORT}`);
});

async function generateFirstQuestion(role: string, difficulty: string) {
  // AI question generation logic
  return { id: '1', text: `Tell me about yourself and why you want to be a ${role}?`, type: 'behavioral' };
}

async function analyzeAnswer(transcript: string, questionId: string) {
  // AI analysis logic
  return { score: 85, feedback: 'Great answer!', improvements: [] };
}

async function getNextQuestion(questionId: string, userId: string) {
  return null; // Returns null when interview is complete
}

export { app, io };

// Updated: 2026-08-13T22:28:00

// Updated: 2026-06-23T22:36:00

// Updated: 2026-10-11T22:10:00

// Updated: 2026-06-03T14:42:00

// Updated: 2026-06-15T15:45:00

// Updated: 2026-11-06T12:54:00

// Updated: 2026-10-14T17:19:00

// Updated: 2026-11-05T10:29:00

// Updated: 2026-08-14T19:19:00

// Updated: 2026-07-03T21:52:00

// Updated: 2026-09-21T20:10:00

// Updated: 2026-05-29T10:06:00

// Updated: 2026-08-13T17:41:00

// Updated: 2026-08-02T20:31:00

// Updated: 2026-07-23T12:27:00

// Updated: 2026-10-07T20:40:00

// Updated: 2026-06-06T09:10:00

// Updated: 2026-10-09T09:43:00

// Updated: 2026-11-07T13:25:00

// Updated: 2026-05-17T22:57:00

// Updated: 2026-09-25T11:17:00

// 2026-05-19 11:00

// 2026-05-20 10:00

// 2026-05-28 11:00

// 2026-05-29 09:00

// 2026-06-02 11:00

// 2026-06-06 09:00

// 2026-06-11 09:30

// 2026-06-17 11:00
