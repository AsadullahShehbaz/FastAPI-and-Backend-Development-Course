from datetime import datetime, timedelta, timezone
from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlmodel import Session, SQLModel, select

from .models import Product, ProductStatus

# The engine = our connection to the database
engine = create_engine(
    url="sqlite:///products.db",                  # dialect + file name
    echo=True,                                    # print every SQL query
    connect_args={"check_same_thread": False},    # SQLite + FastAPI threads
)


def create_db_tables():
    # import the model so it is registered in SQLModel.metadata
    from .models import Product  # noqa: F401
    SQLModel.metadata.create_all(bind=engine)


# Bonus: load the 7 starter products when the table is empty
def seed_products():
    starter = [
        ("Wireless Mouse", 18.99, 42, 1), ("Mechanical Keyboard", 64.99, 18, 2),
        ("USB-C Hub", 29.99, 35, 1), ("Laptop Stand", 39.99, 12, 3),
        ("Webcam", 54.99, 25, 2), ("Bluetooth Speaker", 44.99, 30, 4),
        ("External SSD", 89.99, 10, 5),
    ]
    with Session(engine) as session:
        if session.exec(select(Product)).first() is None:
            for name, price, stock, warehouse in starter:
                session.add(Product(
                    name=name, price=price, stock=stock, warehouse=warehouse,
                    status=ProductStatus.low_stock if stock <= 12 else ProductStatus.active,
                    warranty_until=datetime.now(timezone.utc) + timedelta(days=365),
                ))
            session.commit()


# A fresh session per request. "yield" inside "with" -> opened, then closed
def get_session():
    with Session(bind=engine) as session:
        yield session


# Annotated dependency: write "session: SessionDep" in any endpoint
SessionDep = Annotated[Session, Depends(get_session)]
