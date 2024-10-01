# app/main.py

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from . import database, models

app = FastAPI()


# Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users/", response_model=list[dict])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users
