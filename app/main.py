from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .db import SessionLocal
from .models import Country, State, City

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/countries")
def get_countries(db: Session = Depends(get_db)):
    countries = db.query(Country).all()
    return [{"id": c.id, "name": c.name} for c in countries]

@app.get("/states/{country_id}")
def get_states(country_id: int, db: Session = Depends(get_db)):
    states = db.query(State).filter(State.country_id == country_id).all()
    return [{"id": s.id, "name": s.name} for s in states]

@app.get("/cities/{state_id}")
def get_cities(state_id: int, db: Session = Depends(get_db)):
    cities = db.query(City).filter(City.state_id == state_id).all()
    return [{"id": c.id, "name": c.name} for c in cities]


@app.get("/", response_class=HTMLResponse)
def serve_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
