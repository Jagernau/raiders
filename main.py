from fastapi import FastAPI, HTTPException
from models import FrameWorkModel, Base
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
from typing import Any, List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI
from crud import get_frams, get_fram_from_lang


from schemas import FrameworkSchema
import uvicorn

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
        "https://raiders-production.up.railway.app:8000/",
        "https://raiders-production.up.railway.app/",
        "http://raiders-production.up.railway.app:8000/",

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()



@app.get("/frameworks/", response_model=List[FrameworkSchema])
def read_framss(db: Session = Depends(get_db)):
    frams = get_frams(db)
    return frams



@app.get("/frameworks/{language}", response_model=FrameworkSchema)
def read_frams(language: str, db: Session = Depends(get_db)):
    db_frams = get_fram_from_lang(db, language=language)
    if db_frams is None:
        raise HTTPException(status_code=404, detail="Framework not found")
    return db_frams




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
