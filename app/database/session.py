from fastapi import Depends
from typing_extensions import Annotated
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine,async_sessionmaker
from sqlmodel import SQLModel
from app.config import settings
from app.services.product import ProductService

# 1.Create the database engine asynchronously
engine = create_async_engine(settings.POSTGRES_URL, echo=True)

# 3.Create Session Factory Asynchrously
async_session = async_sessionmaker(bind=engine,class_=AsyncSession,expire_on_commit=False)

# 2. Create tables asynchronously
async def create_db_tables():
    async with engine.begin() as connection:
        await connection.run_sync(SQLModel.metadata.create_all) 

# 4.Dependency
async def get_session():
    async with async_session() as session:
        yield session

