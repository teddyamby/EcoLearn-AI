from fastapi import APIRouter, Request, Cookie, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from ..database import SessionLocal
from ..models import User
from ..templates_engine import templates

router = APIRouter()

CO2_PER_HOUR = 20  # grammes de CO2 / heure (estimation pédagogique)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/dashboard")
def dashboard(
    request: Request,
    user_id: str = Cookie(None),
    db: Session = Depends(get_db)
):
    if not user_id:
        return RedirectResponse("/login", status_code=303)

    user = db.query(User).get(int(user_id))

    # 🔄 Mise à jour CO2 basé sur le temps d'étude
    user.co2_consumed = round(user.study_time * CO2_PER_HOUR, 2)
    db.commit()

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "user": user
        }
    )
