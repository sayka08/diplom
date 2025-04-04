from fastapi import HTTPException
from sqlalchemy.orm import Session
from backend.db.repositories import comment as comment_repo
from backend.db.repositories import post as post_repo
from backend.db.repositories import user as user_repo  # Переименовываем импорт
from backend.schemas.comment import CommentResponse
from backend.db.repositories.comment import get_comments_by_post

def create_comment_service(db: Session, user_id: int, post_id: int, text: str):
    db_post = post_repo.get_post(db, post_id)  # Используем переименованный импорт
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")

    new_comment = comment_repo.create_comment(db, user_id, post_id, text)

    db_post.comments_count += 1
    db.commit()
    db.refresh(new_comment)

    db_user = user_repo.get_user_by_id(db, user_id)  # Используем переименованный импорт

    return CommentResponse(
        id=new_comment.id,
        user_id=user_id,
        post_id=post_id,
        username=db_user.username,
        text=new_comment.text,
        created_at=new_comment.created_at
    )

def get_comments_service(db: Session, post_id: int, skip: int = 0, limit: int = 100):
    comments = get_comments_by_post(db, post_id, skip, limit)

    result = []
    for comment in comments:
        comment_user = user_repo.get_user_by_id(db, comment.user_id)  # Переименовали переменную
        result.append(CommentResponse(
            id=comment.id,
            user_id=comment.user_id,
            post_id=comment.post_id,
            username=comment_user.username,  # Используем переименованную переменную
            text=comment.text,
            created_at=comment.created_at
        ))

    return result

def delete_comment_service(db: Session, comment_id: int, user_id: int):
    comment_to_delete = comment_repo.delete_comment(db, comment_id, user_id)
    if not comment_to_delete:
        raise HTTPException(status_code=404, detail="Comment not found")

    post = comment_to_delete.post
    post.comments_count -= 1
    db.commit()

    return {"message": "Comment deleted successfully"}