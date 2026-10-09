from typing import Annotated
from app.config import settings
from fastapi import Depends

from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel,Session
from .models import Product

# Create the database engine
engine = create_async_engine(settings.DATABASE_URL, echo=True)

async def create_db_tables():
    async with engine.begin() as connection:
        # create_all is SYNC, so run it through run_sync (pass it, don't call it)
        await connection.run_sync(SQLModel.metadata.create_all)

# Session factory (pooling, thread safety). expire_on_commit=False keeps
# objects usable after commit() so refresh()/return still work.
async_session = async_sessionmaker(bind=engine,class_=AsyncSession,expire_on_commit=False,)

# Async generator dependency: one session per request
async def get_session():
    async with async_session() as session:
        yield session

SessionDep = Annotated[Session,Depends(get_session)]
