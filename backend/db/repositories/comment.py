from sqlalchemy.orm import Session
from backend.db.models.comment import Comment

def create_comment(db: Session, user_id: int, post_id: int, text: str):
    comment = Comment(user_id=user_id, post_id=post_id, text=text)
    db.add(comment)
    db.flush()
    return comment

def get_comments_by_post(db: Session, post_id: int, skip: int = 0, limit: int = 100):
    return db.query(Comment).filter(Comment.post_id == post_id)\
                          .offset(skip).limit(limit).all()

def delete_comment(db: Session, comment_id: int, user_id: int):
    comment = db.query(Comment).filter(Comment.id == comment_id,
                                     Comment.user_id == user_id).first()
    if comment:
        db.delete(comment)
    return comment