# app/form_data.py
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from . import schemas, models, crud
from .database import get_db
from .auth_utils import get_current_user

router = APIRouter(prefix="/api/v1")

@router.post("/form-data", response_model=schemas.FormDataResponse)
async def submit_form_data(
    form_data: schemas.FormDataCreate,
    files: list[UploadFile] = File(...),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    try:
        # Save form data to database
        db_form = crud.create_form_data(db, form_data, user_id=current_user.id)
        
        # Handle file uploads
        file_paths = []
        for file in files:
            file_path = f"uploads/{file.filename}"
            with open(file_path, "wb") as buffer:
                buffer.write(await file.read())
            file_paths.append(file_path)
        
        return {
            "status": "success",
            "message": "Form submitted successfully",
            "data": db_form
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))