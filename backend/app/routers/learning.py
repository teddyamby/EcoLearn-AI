from fastapi import APIRouter, Request, Form, Cookie, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Course, User
from ..ai_service import generate_course
from ..templates_engine import templates

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def calculate_co2(duration: str) -> float:
    if "30" in duration:
        return 0.2
    if "1" in duration:
        return 0.5
    if "2" in duration:
        return 1.0
    return 0.3

@router.get("/generator")
def generator(request: Request):
    return templates.TemplateResponse("generator.html", {"request": request})

@router.post("/generator")
def generate(
    request: Request,
    topic: str = Form(...),
    level: str = Form(...),
    time: str = Form(...),
    user_id: str = Cookie(None),
    db: Session = Depends(get_db)
):
    if not user_id:
        return RedirectResponse("/login", status_code=303)

    content = generate_course(topic, level, time)
    co2 = calculate_co2(time)

    course = Course(
        title=topic,
        level=level,
        duration=time,
        content=content,
        co2_generated=co2,
        user_id=int(user_id)
    )

    user = db.query(User).get(int(user_id))
    user.co2_consumed += co2
    user.study_time += 0.5

    db.add(course)
    db.commit()

    return templates.TemplateResponse(
        "learning.html",
        {"request": request, "course": content}
    )
