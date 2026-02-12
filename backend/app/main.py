from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

from .database import Base, engine
from .routers import auth, dashboard, learning, impact
from .templates_engine import templates

app = FastAPI(title="EcoLearn AI")

Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(auth.router)
app.include_router(dashboard.router)
app.include_router(learning.router)
app.include_router(impact.router)

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
