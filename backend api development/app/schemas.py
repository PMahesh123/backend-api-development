from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    phone_number: Optional[str] = None

class LoginRequest(BaseModel):
    phone_number: str
    password: str

class FormDataBase(BaseModel):
    field1: str
    field2: str
    # Add all fields as per the KPA form requirements

class FormDataCreate(FormDataBase):
    pass

class FormDataResponse(FormDataBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    phone_number: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True