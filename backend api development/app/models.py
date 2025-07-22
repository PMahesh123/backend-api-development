# app/models.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from .database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    # other fields...

class FormData(Base):
    __tablename__ = "form_data"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    field1 = Column(String)
    field2 = Column(String)
    # other form fields...
    created_at = Column(DateTime)