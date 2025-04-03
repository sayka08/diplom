from sqlalchemy.orm import Session
from backend.db.models.post import Post

def create_post(db: Session, user_id: int, description: str):
    new_post = Post(
        user_id=user_id,
        description=description
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()

def increment_views(db: Session, post_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        post.views += 1
        db.commit()
        db.refresh(post)
    return post