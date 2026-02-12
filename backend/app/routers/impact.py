from fastapi import APIRouter, Request
from ..templates_engine import templates

router = APIRouter()

@router.get("/impact")
def impact(request: Request):
    return templates.TemplateResponse(
        "impact.html",
        {"request": request}
    )

@router.get("/pricing")
def pricing(request: Request):
    return templates.TemplateResponse(
        "pricing.html",
        {"request": request}
    )

@router.get("/support")
def support(request: Request):
    return templates.TemplateResponse(
        "support.html",
        {"request": request}
    )
