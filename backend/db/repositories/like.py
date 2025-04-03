from sqlalchemy.orm import Session
from backend.db.models.like import Like

def create_like(db: Session, user_id: int, post_id: int):
    like = Like(user_id=user_id, post_id=post_id)
    db.add(like)
    db.flush()
    return like

def delete_like(db: Session, user_id: int, post_id: int):
    like = db.query(Like).filter(
        Like.user_id == user_id,
        Like.post_id == post_id
    ).first()
    if like:
        db.delete(like)
        db.commit()
    return like

def get_like(db: Session, user_id: int, post_id: int):
    return db.query(Like).filter(
        Like.user_id == user_id,
        Like.post_id == post_id
    ).first()