from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from backend.db.session import engine
from dotenv import load_dotenv
from backend.db.models.user import Base
from backend.api.v1.endpoints import auth
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

Base.metadata.create_all(bind=engine)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")

app = FastAPI(
    title="Blog API",
    description="API для блога с аутентификацией",
    openapi_tags=[{"name": "auth", "description": "Аутентификация"}]
)

app.include_router(auth.router, prefix="/api/v1", tags=["auth"])

@app.get("/", dependencies=[Depends(oauth2_scheme)])
async def root():
    return {"message": "Hello, world!"}

@app.get("/test")
async def test():
    return {"message": "Test works!"}