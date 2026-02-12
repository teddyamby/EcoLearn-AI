from fastapi import APIRouter, Request, Form, Cookie, Depends
from sqlalchemy.orm import Session

from ..database import SessionLocal
from ..models import Course
from ..ai_service import generate_course
from ..templates_engine import templates

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/generator")
def generator(request: Request):
    return templates.TemplateResponse("generator.html", {"request": request})

@router.post("/generator")
def generate_course_route(
    request: Request,
    topic: str = Form(...),
    level: str = Form(...),
    time: str = Form(...),
    user_id: str = Cookie(None),
    db: Session = Depends(get_db)
):
    course_content = generate_course(topic, level, time)

    # Sauvegarde du cours
    course = Course(
        user_id=int(user_id),
        topic=topic,
        level=level,
        duration=time,
        content=course_content,
        time_spent=0
    )
    db.add(course)
    db.commit()

    return templates.TemplateResponse(
        "learning.html",
        {
            "request": request,
            "course": course_content
        }
    )
