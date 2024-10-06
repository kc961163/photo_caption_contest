# # api/images/controllers.py

# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session

# from api.utils import crud
# from api.utils.dependencies import get_db
# from api.images import schemas, models
# from api.auth.controllers import get_current_user

# router = APIRouter()

# @router.post("/", response_model=schemas.ImageOut)
# def upload_image(
#     image: schemas.ImageCreate,
#     db: Session = Depends(get_db),
#     current_user: models.User = Depends(get_current_user),
# ):
#     # Create the image record
#     new_image = crud.create_image(db=db, image=image, uploader_id=current_user.id)
#     return new_image

# @router.get("/{image_id}", response_model=schemas.ImageOut)
# def read_image(
#     image_id: int, db: Session = Depends(get_db)
# ):
#     image = crud.get_image(db, image_id=image_id)
#     if not image:
#         raise HTTPException(status_code=404, detail="Image not found")
#     return image

# # Add more image-related endpoints as needed
