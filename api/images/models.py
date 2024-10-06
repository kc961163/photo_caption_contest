# api/images/models.py

from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.orm import relationship

from api.database.database import Base


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    uploaded_at = Column(DateTime, default=datetime.now(timezone.utc))

    captions = relationship("Caption", back_populates="image")
