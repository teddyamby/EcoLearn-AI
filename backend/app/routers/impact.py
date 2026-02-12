from fastapi import APIRouter, Request

router = APIRouter()

@router.get("/impact")
def impact(request: Request):
    return request.app.templates.TemplateResponse(
        "impact.html", {"request": request}
    )
