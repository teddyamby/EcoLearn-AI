from fastapi import APIRouter, Request, Form
from ..ai_service import generate_course
from ..templates_engine import templates

router = APIRouter()

@router.get("/generator")
def generator(request: Request):
    return templates.TemplateResponse(
        "generator.html",
        {"request": request}
    )

@router.post("/generator")
def generate(
    request: Request,
    topic: str = Form(...),
    level: str = Form(...),
    time: str = Form(...)
):
    course = generate_course(topic, level, time)

    return templates.TemplateResponse(
        "learning.html",
        {
            "request": request,
            "course": course
        }
    )
