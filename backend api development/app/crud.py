from sqlalchemy.orm import Session
from . import models, schemas
from .auth_utils import get_password_hash

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_phone(db: Session, phone: str):
    return db.query(models.User).filter(models.User.phone_number == phone).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(
        phone_number=user.phone_number,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_form_data(db: Session, form_data: schemas.FormDataCreate, user_id: int):
    db_form = models.FormData(**form_data.dict(), user_id=user_id)
    db.add(db_form)
    db.commit()
    db.refresh(db_form)
    return db_form

def get_form_data(db: Session, form_id: int):
    return db.query(models.FormData).filter(models.FormData.id == form_id).first()

def get_user_form_data(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.FormData).filter(models.FormData.user_id == user_id).offset(skip).limit(limit).all()