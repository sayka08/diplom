from pydantic import BaseModel
from typing import Optional
from datetime import date

class UserCreate(BaseModel):
    username: str
    password: str

    class Config:
        extra = 'forbid'

class UserLogin(BaseModel):
    username: str
    password: str

    class Config:
        extra = 'forbid'

class UserUpdate(BaseModel):
    name: Optional[str] = None  # "male" или "female"
    surname: Optional[str] = None
    birth_date: Optional[date] = None  # формат ddmmyy, например "010190"
    gender: Optional[str] = None      # "male" или "female"
    phone: Optional[str] = None
    email: Optional[str] = None

    class Config:
        extra = 'forbid'