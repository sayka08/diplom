from backend.db.repositories.like import create_like, delete_like, get_like
from backend.db.repositories.post import get_post
from backend.db.models.post import Post
from fastapi import HTTPException
from sqlalchemy.orm import Session


def like_post(db: Session, user_id: int, post_id: int):
    try:
        post = db.query(Post).filter(Post.id == post_id).first()
        if not post:
            raise HTTPException(status_code=404, detail="Post not found")

        if get_like(db, user_id, post_id):
            raise HTTPException(status_code=400, detail="Already liked")

        create_like(db, user_id, post_id)

        post.likes_count += 1
        db.commit()

        return {"post_id": post_id, "likes_count": post.likes_count}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

def unlike_post(db: Session, user_id: int, post_id: int):
    like = delete_like(db, user_id, post_id)
    if not like:
        raise HTTPException(status_code=404, detail="Like not found")
    return {"post_id": post_id, "likes_count": len(like.post.likes)}