# api/utils/dependencies.py

from sqlalchemy.orm import Session

from api.database.database import SessionLocal  # Absolute import


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
