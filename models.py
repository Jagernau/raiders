from sqlalchemy import Column, Integer, String

from .database import Base


class FrameWorkModel(Base):
    __tablename__ = "users"

    pk = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    language = Column(String, index=True)


    
