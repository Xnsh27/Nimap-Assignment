from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import engine, Base
from models import User, Document, Role, UserRole

from auth.router import router as auth_router
from roles.router import router as roles_router
from documents.router import router as documents_router
from rag.router import router as rag_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(title="FastAPI Application", lifespan=lifespan)

app.include_router(auth_router)
app.include_router(roles_router)
app.include_router(documents_router)
app.include_router(rag_router)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}