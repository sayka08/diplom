from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from backend.db.session import get_db
from backend.schemas.like import LikeResponse
from backend.services.auth_service import get_current_user
from backend.services.like_service import like_post, unlike_post

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")


@router.post("/posts/{post_id}/like", response_model=LikeResponse, tags=["likes"])
async def like_post_endpoint(
    post_id: int,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    current_user = get_current_user(db, token)
    return like_post(db, current_user.id, post_id)

@router.delete("/posts/{post_id}/like", response_model=LikeResponse, tags=["likes"])
async def unlike_post_endpoint(
    post_id: int,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    current_user = get_current_user(db, token)
    return unlike_post(db, current_user.id, post_id)