from fastapi import APIRouter, Request
from ..templates_engine import templates

router = APIRouter()

@router.get("/impact")
def impact(request: Request):
    return templates.TemplateResponse(
        "impact.html",
        {"request": request}
    )
