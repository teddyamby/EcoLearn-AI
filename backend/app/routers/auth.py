from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import RedirectResponse, HTMLResponse
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from datetime import date

from ..database import SessionLocal
from ..models import User
from ..auth import hash_password, verify_password
from ..templates_engine import templates

# ✅ ROUTER DOIT ÊTRE DÉFINI AVANT LES DÉCORATEURS
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -------- REGISTER --------

@router.get("/register")
def register_form(request: Request):
    return templates.TemplateResponse(
        "register.html",
        {"request": request}
    )

@router.post("/register")
def register_user(
    request: Request,
    first_name: str = Form(...),
    last_name: str = Form(...),
    username: str = Form(...),
    birth_date: date = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    try:
        user = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            birth_date=birth_date,
            password_hash=hash_password(password)
        )
        db.add(user)
        db.commit()

    except IntegrityError:
        db.rollback()
        return templates.TemplateResponse(
            "register.html",
            {
                "request": request,
                "error": "Ce nom d’utilisateur existe déjà."
            }
        )

    except Exception:
        db.rollback()
        return templates.TemplateResponse(
            "register.html",
            {
                "request": request,
                "error": "Erreur interne. Veuillez réessayer."
            }
        )

    return RedirectResponse("/login", status_code=303)

# -------- LOGIN --------

@router.get("/login")
def login_form(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {"request": request}
    )

@router.post("/login")
def login_user(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.username == username).first()

    if not user or not verify_password(password, user.password_hash):
        return HTMLResponse("Identifiants invalides", status_code=401)

    response = RedirectResponse("/dashboard", status_code=303)
    response.set_cookie(
        key="user_id",
        value=str(user.id),
        httponly=True,
        secure=True  # OK sur Render (HTTPS)
    )
    return response




