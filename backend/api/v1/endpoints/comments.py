from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from backend.db.session import get_db
from backend.schemas.comment import CommentCreate, CommentResponse
from backend.services.auth_service import get_current_user
from backend.services import comment_service

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")

@router.post("/posts/{post_id}/comments", response_model=CommentResponse, tags=["comments"])
async def create_comment(
    post_id: int,
    comment_data: CommentCreate,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    current_user = get_current_user(db, token)
    return comment_service.create_comment_service(
        db, current_user.id, post_id, comment_data.text
    )

@router.get("/posts/{post_id}/comments", response_model=list[CommentResponse], tags=["comments"])
async def get_comments(
    post_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return comment_service.get_comments_service(db, post_id, skip, limit)

@router.delete("/comments/{comment_id}", tags=["comments"])
async def delete_comment(
    comment_id: int,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    current_user = get_current_user(db, token)
    return comment_service.delete_comment_service(db, comment_id, current_user.id)