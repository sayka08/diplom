from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.services.auth_service import get_current_user
from backend.db.session import get_db
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")

@router.get("/me")
async def read_users_me(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    current_user = get_current_user(db, token)
    return {"username": current_user.username}