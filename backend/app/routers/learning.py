from fastapi import APIRouter, Request, Form
from ..ai_service import generate_course

router = APIRouter()

@router.get("/generator")
def generator(request: Request):
    return request.app.templates.TemplateResponse(
        "generator.html", {"request": request}
    )

@router.post("/generator")
def generate(
    request: Request,
    topic: str = Form(...),
    level: str = Form(...),
    time: str = Form(...)
):
    course = generate_course(topic, level, time)
    return request.app.templates.TemplateResponse(
        "learning.html",
        {"request": request, "course": course}
    )
