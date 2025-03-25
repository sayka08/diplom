from typing import Optional
from sqlalchemy.orm import Session
from backend.db.models.user import User

def get_user_by_username(db: Session, username: str) -> Optional[User]:
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, username: str, password_hash: str) -> User:
    new_user = User(username=username, password_hash=password_hash)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

