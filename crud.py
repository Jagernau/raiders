from sqlalchemy.orm import Session
from models import FrameWorkModel


def get_fram_from_lang(db: Session, language: str):
    return db.query(FrameWorkModel).filter(FrameWorkModel.language == language).first()

def get_frams(db: Session):
    return db.query(FrameWorkModel).all()
