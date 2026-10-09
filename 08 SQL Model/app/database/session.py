from fastapi import Depends
from typing_extensions import Annotated

from sqlalchemy import create_engine
from sqlmodel import SQLModel,Session
from .models import Product

# Create the database engine
engine = create_engine("sqlite:///database.db",echo=True,connect_args={"check_same_thread":False})

def create_db_tables():
    SQLModel.metadata.create_all(bind=engine) 

def get_session():
    with Session(engine) as session:
        yield session

SessionDep : Annotated[Session,Depends(get_session)]