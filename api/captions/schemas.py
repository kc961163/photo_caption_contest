# # api/captions/schemas.py

# from typing import Optional
# from pydantic import BaseModel

# class CaptionBase(BaseModel):
#     text: str

# class CaptionCreate(CaptionBase):
#     image_id: int

# class CaptionOut(CaptionBase):
#     id: int
#     created_at: str
#     user_id: int
#     image_id: int
#     likes: int

#     class Config:
#         orm_mode = True
