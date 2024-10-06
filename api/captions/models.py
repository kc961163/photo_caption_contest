# api/captions/models.py

from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

from api.database.database import Base


class Caption(Base):
    __tablename__ = "captions"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    image_id = Column(Integer, ForeignKey("images.id"), nullable=False)
    likes = Column(Integer, default=0)

    owner = relationship("User", back_populates="captions")
    image = relationship("Image", back_populates="captions")
