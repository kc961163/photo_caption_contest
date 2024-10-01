# app/models.py

from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_admin = Column(Integer, default=0)

    captions = relationship("Caption", back_populates="owner")


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    uploaded_at = Column(DateTime, default=datetime.utcnow)

    captions = relationship("Caption", back_populates="image")


class Caption(Base):
    __tablename__ = "captions"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    image_id = Column(Integer, ForeignKey("images.id"), nullable=False)
    likes = Column(Integer, default=0)

    owner = relationship("User", back_populates="captions")
    image = relationship("Image", back_populates="captions")
