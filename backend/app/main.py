from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .database import Base, engine
from .routers import auth, dashboard, learning, impact

app = FastAPI(title="EcoLearn AI")

Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

app.include_router(auth.router)
app.include_router(dashboard.router)
app.include_router(learning.router)
app.include_router(impact.router)

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
