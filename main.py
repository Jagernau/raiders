from fastapi import FastAPI
from raiders import  models, schemas
from raiders.database import SessionLocal, engine
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "*"
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
    schema=schemas.FrameworkSchema,
    create_schema=schemas.FrameworkCreateSchema,
    db_model=models.FrameWorkModel,
    db=get_db,
    prefix='frameworks'
)

app.include_router(router)
