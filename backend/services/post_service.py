from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from backend.db.repositories.post import create_post, get_post, increment_views
from backend.db.repositories.user import get_user_by_id
from backend.schemas.post import PostResponse


def create_post_service(db: Session, user_id: int, description: str):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    post = create_post(db, user_id, description)
    return PostResponse(
        id=post.id,
        user_id=user_id,
        username=user.username,
        name=user.name,
        description=post.description,
        created_at=post.created_at,
        views=post.views,
        comments_count=post.comments_count,
        likes_count=post.likes_count
    )


def get_post_service(db: Session, post_id: int):
    post = get_post(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    user = get_user_by_id(db, post.user_id)
    increment_views(db, post_id)

    return PostResponse(
        id=post.id,
        user_id=post.user_id,
        username=user.username,
        name=user.name,
        description=post.description,
        created_at=post.created_at,
        views=post.views + 1,
        comments_count=post.comments_count,
        likes_count=post.likes_count
    )