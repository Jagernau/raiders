from sqlalchemy.orm import Session
from models import FrameWorkModel


def get_fram_from_lang(db: Session, language: str):
    return db.query(FrameWorkModel).filter(FrameWorkModel.language == language).first()

def get_frams(db: Session, skip: int = 0, limit: int = 100):
    return db.query(FrameWorkModel).offset(skip).limit(limit).all()
