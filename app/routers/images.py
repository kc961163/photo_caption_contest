# app/routers/images.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, models, schemas
from ..dependencies import get_db
from ..routers.auth import get_current_user

router = APIRouter(prefix="/images", tags=["Images"])

# @router.post("/", response_model=schemas.ImageOut)
# def upload_image(image: schemas.ImageCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
#     # Implement image upload logic
#     # new_image = crud.create_image(db=db, image=image, uploader_id=current_user.id)
#     # return new_image
#     pass

# Add more image-related endpoints
