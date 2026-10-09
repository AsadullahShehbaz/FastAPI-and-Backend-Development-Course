from fastapi import Depends
from typing_extensions import Annotated
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlmodel import SQLModel,Session
from .models import Product
from app.config import settings

# Create the database engine
engine = create_async_engine(settings.POSTGRES_URL, echo=True, connect_args={"check_same_thread": False})

sessionmaker    

def create_db_tables():
    SQLModel.metadata.create_all(bind=engine) 

async def get_session():
    async with async_session() as session:
        yield session

SessionDep : Annotated[Session,Depends(get_session)]