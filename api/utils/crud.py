# api/utils/crud.py

from typing import Optional

from sqlalchemy.orm import Session

from api.auth.models import User
from api.auth.schemas import UserCreate

# from api.captions.models import Caption
# from api.captions.schemas import CaptionCreate
# from api.images.models import Image
# from api.images.schemas import ImageCreate
from api.utils import utils


# User CRUD operations
def get_user_by_email(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter(User.email == email).first()


def get_user_by_username(db: Session, username: str) -> Optional[User]:
    return db.query(User).filter(User.username == username).first()


def get_user(db: Session, user_id: int) -> Optional[User]:
    return db.query(User).filter(User.id == user_id).first()


def create_user(db: Session, user: UserCreate) -> User:
    hashed_password = utils.get_password_hash(user.password)
    db_user = User(
        username=user.username, email=user.email, hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Image CRUD operations
# def get_image(db: Session, image_id: int) -> Optional[Image]:
#     return db.query(Image).filter(Image.id == image_id).first()

# def create_image(db: Session, image: ImageCreate, uploader_id: int) -> Image:
#     db_image = Image(
#         url=image.url,
#         description=image.description,
#         uploader_id=uploader_id  # Assuming you have this field in Image model
#     )
#     db.add(db_image)
#     db.commit()
#     db.refresh(db_image)
#     return db_image

# # Caption CRUD operations
# def get_caption(db: Session, caption_id: int) -> Optional[Caption]:
#     return db.query(Caption).filter(Caption.id == caption_id).first()

# def create_caption(db: Session, caption: CaptionCreate, user_id: int) -> Caption:
#     db_caption = Caption(
#         text=caption.text,
#         image_id=caption.image_id,
#         user_id=user_id
#     )
#     db.add(db_caption)
#     db.commit()
#     db.refresh(db_caption)
#     return db_caption
