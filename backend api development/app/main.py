from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine
from . import models
from .routers import auth, form_data

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="KPA Form Data API", version="1.0.0")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(form_data.router)

@app.get("/")
def read_root():
    return {"message": "KPA Form Data API is running"}