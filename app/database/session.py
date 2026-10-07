from typing import Annotated
from fastapi import Depends
from sqlalchemy import create_engine
from sqlmodel import SQLModel,Session

# The engine = our connection to the database
engine = create_engine(
    url="sqlite:///products.db",
    # dialect + file name
    echo=True,
    connect_args={"check_same_thread": False},
)

def create_db_tables():
    from .models import Product 
    SQLModel.metadata.create_all(bind=engine)

def get_session():
    with Session(bind=engine) as session:
        yield session
# Annotated dependency: write "session: SessionDep" in any endpoint
SessionDep = Annotated[Session, Depends(get_session)]