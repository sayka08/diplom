from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from backend.db.session import get_db
from backend.services.auth_service import get_current_user
from backend.db.models.user import User
from backend.schemas.auth import UserUpdate
from backend.db.repositories.user import get_user_by_id, update_user

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")

@router.get("/me", tags=["users"])
async def read_users_me(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    current_user = get_current_user(db, token)
    return {
        "id": current_user.id,
        "username": current_user.username,
        "name": current_user.name,
        "surname": current_user.surname,
        "birth_date": current_user.birth_date,
        "gender": current_user.gender,
        "phone": current_user.phone,
        "email": current_user.email,
        "created_at": current_user.created_at
    }

@router.get("/{user_id}", tags=["users"])
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "id": user.id,
        "username": user.username,
        "name": user.name,
        "surname": user.surname,
        "birth_date": user.birth_date,
        "gender": user.gender,
        "phone": user.phone,
        "email": user.email,
        "created_at": user.created_at
    }

@router.put("/{user_id}", tags=["users"])
async def update_user_endpoint(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    update_data = user_update.dict(exclude_unset=True)
    updated_user = update_user(db, user_id, update_data)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "id": updated_user.id,
        "username": updated_user.username,
        "name": updated_user.name,
        "surname": updated_user.surname,
        "birth_date": updated_user.birth_date,
        "gender": updated_user.gender,
        "phone": updated_user.phone,
        "email": updated_user.email,
        "created_at": updated_user.created_at
    }