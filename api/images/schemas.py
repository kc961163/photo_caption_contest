# # api/images/schemas.py

# from typing import Optional
# from pydantic import BaseModel, HttpUrl

# class ImageBase(BaseModel):
#     url: HttpUrl
#     description: Optional[str] = None

# class ImageCreate(ImageBase):
#     pass

# class ImageOut(ImageBase):
#     id: int
#     uploaded_at: str

#     class Config:
#         orm_mode = True
