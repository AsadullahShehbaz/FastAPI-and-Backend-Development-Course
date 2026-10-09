# app/database/session.py
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from app.config import settings

engine = create_async_engine(
    url=settings.POSTGRES_URL,
    echo=True,
)
async def create_db_tables():
    async with engine.begin() as connection:
        from app.database.models import Product  # ensure registered
        await connection.run_sync(SQLModel.metadata.create_all)

asyncio.run(create_db_tables())