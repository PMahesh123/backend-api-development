# app/auth.py
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from . import schemas, models, crud
from .database import get_db
from .auth_utils import create_access_token, verify_password

router = APIRouter(prefix="/api/v1/auth")

@router.post("/login", response_model=schemas.Token)
async def login(
    form_data: schemas.LoginRequest,
    db: Session = Depends(get_db)
):
    user = crud.get_user_by_phone(db, phone=form_data.phone_number)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=400,
            detail="Incorrect phone number or password"
        )
    
    access_token = create_access_token(data={"sub": user.phone_number})
    return {"access_token": access_token, "token_type": "bearer"}