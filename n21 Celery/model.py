from uuid import UUID, uuid4
from pydantic import Field
from sqlalchemy import Column
from sqlmodel import Relationship, SQLModel
from datetime import datetime


class Order(SQLModel, table=True):
    __tablename__ = "order"

    shipment_id: UUID = Field(foreign_key="shipment.id", primary_key=True)
    product_id: UUID = Field(foreign_key="product.id", primary_key=True)

    # extra fields: properties of the relationship
    created_at: datetime = Field(default_factory=datetime.now)
    quantity: int = Field(default=1)

    shipment: "Shipment" = Relationship(back_populates="orders")
    product: "Product" = Relationship(back_populates="orders")


class Product(SQLModel, table=True):
    __tablename__ = "product"

    id: UUID = Field(
        sa_column=Column(postgresql.UUID, default=uuid4, primary_key=True)
    )
    title: str
    description: str
    price: int
    weight: float

    orders: list[Order] = Relationship(back_populates="product")


class Shipment(SQLModel, table=True):
    # ... existing fields and relationships (including tags)

    orders: list[Order] = Relationship(back_populates="shipment")
