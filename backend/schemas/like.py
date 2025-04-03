from pydantic import BaseModel

class LikeResponse(BaseModel):
    post_id: int
    likes_count: int

    class Config:
        orm_mode = True