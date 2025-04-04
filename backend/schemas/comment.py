from pydantic import BaseModel
from datetime import datetime

class CommentCreate(BaseModel):
    text: str

class CommentResponse(BaseModel):
    id: int
    user_id: int
    post_id: int
    username: str
    text: str
    created_at: datetime

    class Config:
        from_attributes = True