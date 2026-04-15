from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
import uuid

from app.database import get_db
from app.models.resume import ResumeCreate, ResumeUpdate, ResumeResponse
from app.services.ai_service import AIResumeService
from app.services.pdf_service import PDFService
from app.auth.dependencies import get_current_user

router = APIRouter()
ai_service = AIResumeService()
pdf_service = PDFService()


@router.post("/generate", response_model=ResumeResponse, status_code=status.HTTP_201_CREATED)
async def generate_resume(
    data: ResumeCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """Generate a complete AI-powered resume."""
    try:
        # Generate AI content
        summary = await ai_service.generate_summary(
            experience=data.experience,
            skills=data.skills,
            target_role=data.target_role
        )
        
        # Enhance each experience entry
        enhanced_experiences = []
        for exp in data.experience:
            bullets = await ai_service.enhance_experience(
                job_title=exp.get("title", ""),
                company=exp.get("company", ""),
                description=exp.get("description", ""),
                achievements=exp.get("achievements", [])
            )
            enhanced_experiences.append({**exp, "bullets": bullets})
        
        # Build resume object
        resume_data = {
            "id": str(uuid.uuid4()),
            "user_id": current_user.id,
            "name": data.name,
            "email": data.email,
            "phone": data.phone,
            "linkedin": data.linkedin,
            "github": data.github,
            "summary": summary,
            "experience": enhanced_experiences,
            "education": data.education,
            "skills": data.skills,
            "projects": data.projects,
            "certifications": data.certifications,
            "template": data.template or "modern",
            "target_role": data.target_role
        }
        
        # Save to DB in background
        background_tasks.add_task(save_resume_to_db, resume_data, db)
        
        return ResumeResponse(**resume_data)
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to generate resume: {str(e)}"
        )


@router.post("/{resume_id}/optimize")
async def optimize_resume(
    resume_id: str,
    job_description: str,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """Optimize resume for a specific job description."""
    resume = await get_resume_by_id(resume_id, db)
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")
    
    if resume.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    optimizations = await ai_service.optimize_for_job(resume, job_description)
    return {
        "resume_id": resume_id,
        "optimizations": optimizations,
        "message": "Review suggestions and apply them to improve ATS score"
    }


@router.get("/{resume_id}", response_model=ResumeResponse)
async def get_resume(
    resume_id: str,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """Get a specific resume."""
    resume = await get_resume_by_id(resume_id, db)
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")
    return resume


@router.post("/{resume_id}/export")
async def export_resume(
    resume_id: str,
    format: str = "pdf",
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """Export resume as PDF or DOCX."""
    resume = await get_resume_by_id(resume_id, db)
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")
    
    if format == "pdf":
        file_url = await pdf_service.generate_pdf(resume)
    elif format == "docx":
        file_url = await pdf_service.generate_docx(resume)
    else:
        raise HTTPException(status_code=400, detail="Format must be 'pdf' or 'docx'")
    
    return {"download_url": file_url, "format": format}


@router.post("/cover-letter")
async def generate_cover_letter(
    resume_id: str,
    job_description: str,
    company_name: str,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """Generate a tailored cover letter."""
    resume = await get_resume_by_id(resume_id, db)
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")
    
    cover_letter = await ai_service.generate_cover_letter(
        resume_data=resume,
        job_description=job_description,
        company_name=company_name
    )
    
    return {"cover_letter": cover_letter, "resume_id": resume_id}


async def save_resume_to_db(resume_data: dict, db: AsyncSession):
    """Background task to save resume to database."""
    pass  # Implementation with SQLAlchemy


async def get_resume_by_id(resume_id: str, db: AsyncSession):
    """Fetch resume from database."""
    pass  # Implementation with SQLAlchemy

# Updated: 2026-08-08T12:26:00

# Updated: 2026-10-04T10:41:00

# Updated: 2026-05-30T12:04:00

# Updated: 2026-09-08T17:03:00

# Updated: 2026-07-17T18:33:00

# Updated: 2026-09-20T14:08:00

# Updated: 2026-10-06T10:08:00

# Updated: 2026-10-15T10:35:00

# Updated: 2026-10-11T09:24:00

# Updated: 2026-05-16T16:10:00

# Updated: 2026-08-18T18:43:00

# Updated: 2026-10-26T15:30:00

# 2026-05-14 10:00

# 2026-05-15 11:00

# 2026-05-16 09:00

# 2026-07-01 09:00

# 2026-07-04 09:00

# 2026-07-08 11:00

# 2026-07-23 09:30
