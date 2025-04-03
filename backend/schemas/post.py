from datetime import datetime
from pydantic import BaseModel

class PostCreate(BaseModel):
    description: str

class PostResponse(BaseModel):
    id: int
    user_id: int
    username: str
    name: str
    description: str
    created_at: datetime
    views: int
    comments_count: int
    likes_count: int

    class Config:
        orm_mode = True