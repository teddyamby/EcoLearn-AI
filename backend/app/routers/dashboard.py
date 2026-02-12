from fastapi import APIRouter, Request, Cookie, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from ..database import SessionLocal
from ..models import User, Course
from ..templates_engine import templates

router = APIRouter()

# -----------------------------
# Dépendance DB
# -----------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -----------------------------
# Dashboard principal
# -----------------------------
@router.get("/dashboard")
def dashboard(
    request: Request,
    user_id: str = Cookie(None),
    db: Session = Depends(get_db)
):
    if not user_id:
        return RedirectResponse("/login", status_code=303)

    user = db.query(User).filter(User.id == int(user_id)).first()

    if not user:
        return RedirectResponse("/login", status_code=303)

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "user": user
        }
    )

# -----------------------------
# Historique des cours
# -----------------------------
@router.get("/my-courses")
def my_courses(
    request: Request,
    user_id: str = Cookie(None),
    db: Session = Depends(get_db)
):
    if not user_id:
        return RedirectResponse("/login", status_code=303)

    courses = (
        db.query(Course)
        .filter(Course.user_id == int(user_id))
        .order_by(Course.created_at.desc())
        .all()
    )

    return templates.TemplateResponse(
        "my_courses.html",
        {
            "request": request,
            "courses": courses
        }
    )
