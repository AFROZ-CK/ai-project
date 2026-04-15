from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from contextlib import asynccontextmanager
import uvicorn
import logging

from app.routes import resume, auth, analyze
from app.database import init_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting AI Resume Builder API...")
    await init_db()
    yield
    logger.info("Shutting down...")


app = FastAPI(
    title="AI Resume Builder API",
    description="GPT-4 powered resume generation and optimization API",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://ai-resume-builder.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(GZipMiddleware, minimum_size=1000)

app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(resume.router, prefix="/api/resume", tags=["Resume"])
app.include_router(analyze.router, prefix="/api/analyze", tags=["Analysis"])


@app.get("/")
async def root():
    return {
        "message": "AI Resume Builder API",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "ai-resume-builder"}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

# Updated: 2026-11-20T14:20:00

# Updated: 2026-09-17T20:48:00

# Updated: 2026-10-11T16:46:00

# Updated: 2026-08-10T09:02:00

# Updated: 2026-07-15T11:42:00

# Updated: 2026-07-13T12:13:00

# Updated: 2026-08-19T14:16:00

# Updated: 2026-09-07T16:48:00

# Updated: 2026-06-28T13:48:00

# Updated: 2026-09-25T09:05:00

# Updated: 2026-06-17T19:34:00

# Updated: 2026-10-01T14:06:00

# Updated: 2026-07-21T13:12:00

# Updated: 2026-11-13T21:00:00

# Updated: 2026-07-11T13:14:00

# Updated: 2026-09-13T12:30:00

# 2026-05-10 14:30

# 2026-05-30 09:30

# 2026-06-02 10:00

# 2026-06-03 11:00

# 2026-06-04 09:30

# 2026-06-05 10:00

# 2026-06-09 10:30

# 2026-06-10 11:00

# 2026-06-12 10:00

# 2026-06-30 10:00

# 2026-07-14 10:30

# 2026-07-15 11:00

# 2026-07-22 11:00

# 2026-07-25 09:00
