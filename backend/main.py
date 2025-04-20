from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from backend.db.session import engine
from backend.db.models.user import Base
from backend.api.v1.endpoints import auth, users, posts, like, comments
from fastapi.middleware.cors import CORSMiddleware
import os

# Проверяем DATABASE_URL
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL not set in environment variables")

# Создаём таблицы
Base.metadata.create_all(bind=engine)

# Настраиваем OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")

# Создаём приложение
app = FastAPI(
    title="Blog API",
    description="API для блога с аутентификацией",
    openapi_tags=[{"name": "auth", "description": "Аутентификация"}]
)

# Настраиваем CORS
origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # Разрешаем фронтенд
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем роутеры
app.include_router(auth.router, prefix="/api/v1", tags=["auth"])
app.include_router(users.router, prefix="/api/v1", tags=["users"])
app.include_router(posts.router, prefix="/api/v1", tags=["posts"])
app.include_router(like.router, prefix="/api/v1", tags=["likes"])
app.include_router(comments.router, prefix="/api/v1", tags=["comments"])