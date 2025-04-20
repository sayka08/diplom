# backend/services/post_service.py
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from backend.db.repositories.post import create_post, get_post, increment_views
from backend.db.repositories.user import get_user_by_id
from backend.schemas.post import PostResponse
from backend.db.models.post import Post  # Добавили импорт

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

def get_posts_service(db: Session, skip: int = 0, limit: int = 100):
    posts = db.query(Post).offset(skip).limit(limit).all()
    result = []
    for post in posts:
        user = get_user_by_id(db, post.user_id)
        result.append(
            PostResponse(
                id=post.id,
                user_id=post.user_id,
                username=user.username,
                name=user.name,
                description=post.description,
                created_at=post.created_at,
                views=post.views,
                comments_count=post.comments_count,
                likes_count=post.likes_count
            )
        )
    return result