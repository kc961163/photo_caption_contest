# api/users/schemas.py

from typing import List, Optional

from pydantic import BaseModel


class UserProfileBase(BaseModel):
    bio: Optional[str] = None


class UserProfileCreate(UserProfileBase):
    user_id: int


class UserProfileOut(UserProfileBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
