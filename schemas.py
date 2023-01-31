from pydantic import BaseModel

class FrameworkCreateSchema(BaseModel):
    name: str
    language: float



class FrameworkSchema(FrameworkCreateSchema):
    pk: int

    class Config:
        orm_mode = True
