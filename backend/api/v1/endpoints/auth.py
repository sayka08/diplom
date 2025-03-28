from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.services.auth_service import login_user, register_user, get_current_user
from backend.db.session import get_db
from backend.schemas.auth import UserCreate, UserLogin
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")

@router.post("/register", tags=["auth"])
async def register(user: UserCreate, db: Session = Depends(get_db)):
    new_user = register_user(db, user.username, user.password)
    return {
        "message": "User registered seccuessfully",
        "id": new_user.id,
        "username": new_user.username
    }

@router.post("/login", tags=["auth"])
async def login(user: UserLogin, db: Session = Depends(get_db)):
    token = login_user(db, user.username, user.password)
    current_user = get_current_user(db, token)
    return {
        "message": "User logged in successfully",
        "id": current_user.id,
        "access_token": token,
        "token_type": "bearer"
    }

@router.post("/logout", tags=["auth"])
async def logout():
    return {"message": "User logged out successfully"}
