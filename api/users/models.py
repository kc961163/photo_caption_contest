# api/users/models.py

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from api.database.database import Base


class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)
    bio = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="profile")
