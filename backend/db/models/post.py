from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.db.base import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    views = Column(Integer, default=0)
    comments_count = Column(Integer, default=0)
    likes_count = Column(Integer, default=0)
    likes = relationship("Like", backref="post", lazy="dynamic")
    comments_count = Column(Integer, default=0)
    comments = relationship("Comment", backref="post", cascade="all, delete")