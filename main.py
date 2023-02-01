from fastapi import FastAPI
from models import FrameWorkModel, Base
from database import SessionLocal, engine
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from fastapi.middleware.cors import CORSMiddleware

from schemas import FrameworkCreateSchema, FrameworkSchema
import uvicorn

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
        "https://raiders-production.up.railway.app:8000/",
        "https://raiders-production.up.railway.app:8000/",

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


router = SQLAlchemyCRUDRouter(
    schema=FrameworkSchema,
    create_schema=FrameworkCreateSchema,
    db_model=FrameWorkModel,
    db=get_db,
    prefix='frameworks'
)

app.include_router(router)

