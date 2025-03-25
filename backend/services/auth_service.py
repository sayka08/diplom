from fastapi import HTTPException
from sqlalchemy.orm import Session
from backend.db.models.user import User
from backend.db.repositories.user import (
    get_user_by_username,
    create_user,
)
from backend.core.security import (
    hash_password,
    verify_password,
    create_access_token,
    decode_access_token
)
import jwt


def register_user(db: Session, username: str, password: str) -> User:
    existing_user = get_user_by_username(db, username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed = hash_password(password)
    new_user = create_user(db, username, hashed)
    return new_user


def login_user(db: Session, username: str, password: str) -> str:
    db_user = get_user_by_username(db, username)
    if not db_user or not verify_password(password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return create_access_token({"sub": username})


def get_current_user(db: Session, token: str) -> User:
    try:
        payload = decode_access_token(token)
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except (jwt.PyJWTError, KeyError):
        raise HTTPException(status_code=401, detail="Invalid token")

    user = get_user_by_username(db, username)
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    return user
