from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from backend.db.session import get_db
from backend.services.post_service import create_post_service, get_post_service
from backend.schemas.post import PostCreate, PostResponse
from backend.services.auth_service import get_current_user

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")

@router.post("/posts", response_model=PostResponse, tags=["posts"], status_code=status.HTTP_200_OK)
async def create_post(
    post_data: PostCreate,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    try:
        current_user = get_current_user(db, token)
        return create_post_service(
            db,
            current_user.id,
            post_data.description
        )
    except Exception as e:
        return {"Error occured: ", e}

@router.get("/posts/{post_id}", response_model=PostResponse, tags=["posts"])
async def read_post(
    post_id: int,
    db: Session = Depends(get_db)
):
    try:
        return get_post_service(
            db,
            post_id
        )
    except Exception as e:
        return {"Error occured: ", e}