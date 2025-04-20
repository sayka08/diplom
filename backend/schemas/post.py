from datetime import datetime
from pydantic import BaseModel
from typing import Optional  # Добавляем импорт Optional

class PostCreate(BaseModel):
    description: str

class PostResponse(BaseModel):
    id: int
    user_id: int
    username: str
    name: Optional[str] = None  # Теперь name может быть None
    description: str
    created_at: datetime
    views: int
    comments_count: int
    likes_count: int

    class Config:
        from_attributes = True