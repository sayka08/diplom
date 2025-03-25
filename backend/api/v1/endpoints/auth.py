from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.services.auth_service import login_user, register_user, get_current_user
from backend.db.session import get_db
from backend.schemas.auth import UserCreate, UserLogin
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")

@router.post("/register")
async def register(user: UserCreate, db: Session = Depends(get_db)):
    new_user = register_user(db, user.username, user.password)
    return {"message": "User registered", "username": new_user.username}

@router.post("/login")
async def login(user: UserLogin, db: Session = Depends(get_db)):
    token = login_user(db, user.username, user.password)
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me")
async def read_users_me(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    current_user = get_current_user(db, token)
    return {"username": current_user.username}