from datetime import datetime
from sqlmodel import SQLModel, Field, Session
from sqlalchemy import create_engine
from .models import Product, ProductCategory

engine = create_engine(
    "sqlite:///products.db",
    echo=True,
    connect_args={"check_same_thread": False}
)


def create_db_tables():
    SQLModel.metadata.create_all(bind=engine)


# Create tables
create_db_tables()


# 5 sample products
products = [
    Product(
        name="Wireless Headphones",
        price=59.99,
        stock=25,
        category=ProductCategory.ELECTRONICS
    ),
    Product(
        name="Gaming PC",
        price=19.99,
        stock=50,
        category=ProductCategory.ELECTRONICS
    ),
    Product(
        name="Smartwatch",
        price=34.99,
        stock=30,
        category=ProductCategory.ACCESSORIES
    ),
    Product(
        name="Mechanical Keyboard",
        price=89.99,
        stock=15,
        category=ProductCategory.PERIPHERALS
    ),
    Product(
        name="USB-C Monitor",
        price=249.99,
        stock=10,
        category=ProductCategory.ELECTRONICS
    )
]


# Add products to database
session = Session(engine)
session.add_all(products)
session.commit()

# Check product with ID 1
product = session.get(Product, 1)
print(product)