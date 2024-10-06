# # api/captions/controllers.py

# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session

# from api.utils import crud
# from api.utils.dependencies import get_db
# from api.captions import schemas, models
# from api.auth.controllers import get_current_user

# router = APIRouter()

# @router.post("/", response_model=schemas.CaptionOut)
# def create_caption(
#     caption: schemas.CaptionCreate,
#     db: Session = Depends(get_db),
#     current_user: models.User = Depends(get_current_user),
# ):
#     # Check if the image exists
#     image = crud.get_image(db, image_id=caption.image_id)
#     if not image:
#         raise HTTPException(status_code=404, detail="Image not found")

#     # Create the caption
#     new_caption = crud.create_caption(db=db, caption=caption, user_id=current_user.id)
#     return new_caption

# @router.get("/{caption_id}", response_model=schemas.CaptionOut)
# def read_caption(
#     caption_id: int, db: Session = Depends(get_db)
# ):
#     caption = crud.get_caption(db, caption_id=caption_id)
#     if not caption:
#         raise HTTPException(status_code=404, detail="Caption not found")
#     return caption

# # Add more caption-related endpoints as needed
