# backend/services/auth_service.py
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
import logging

# Настраиваем логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def register_user(db: Session, username: str, password: str) -> User:
    logger.info(f"Registering user: {username}")
    existing_user = get_user_by_username(db, username)
    if existing_user:
        logger.error(f"Username already exists: {username}")
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed = hash_password(password)
    new_user = create_user(db, username, hashed)
    logger.info(f"User registered successfully: {username}")
    return new_user

def login_user(db: Session, username: str, password: str) -> str:
    logger.info(f"Attempting login for user: {username}")
    db_user = get_user_by_username(db, username)
    if not db_user:
        logger.error(f"User not found: {username}")
        raise HTTPException(status_code=401, detail="Invalid username or password")

    if not verify_password(password, db_user.password_hash):
        logger.error(f"Invalid password for user: {username}")
        raise HTTPException(status_code=401, detail="Invalid username or password")

    token = create_access_token({"sub": username})
    logger.info(f"Login successful for user: {username}")
    return token

def get_current_user(db: Session, token: str) -> User:
    logger.info("Verifying token")
    try:
        payload = decode_access_token(token)
        username: str = payload.get("sub")
        if username is None:
            logger.error("Invalid token: no username in payload")
            raise HTTPException(status_code=401, detail="Invalid token")
    except (jwt.PyJWTError, KeyError) as e:
        logger.error(f"Invalid token: {str(e)}")
        raise HTTPException(status_code=401, detail="Invalid token")

    user = get_user_by_username(db, username)
    if user is None:
        logger.error(f"User not found for token: {username}")
        raise HTTPException(status_code=401, detail="User not found")
    logger.info(f"User verified: {username}")
    return user