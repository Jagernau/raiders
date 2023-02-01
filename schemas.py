from pydantic import BaseModel

class FrameworkCreateSchema(BaseModel):
    name: str
    language: str



class FrameworkSchema(FrameworkCreateSchema):
    pk: int

    class Config:
        orm_mode = True
