from datetime import datetime, timezone
from uuid import uuid4,UUID
from typing import List
from sqlalchemy import Column
from sqlalchemy.dialects import postgresql
from sqlmodel import Relationship, SQLModel,Field
from pydantic import EmailStr

class Product(SQLModel, table=True):
    __tablename__ = "products"
    id: UUID = Field(sa_column=Column(
        postgresql.UUID,
        primary_key=True,
        default=uuid4
    ))
    name: str = Field(max_length=100)
    price: float = Field(gt=0)
    stock: int = Field(gt=0)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    seller_id: UUID = Field(foreign_key="seller.id")

    seller: "Seller" = Relationship(back_populates="product",sa_relationship_kwargs={"lazy":"selectin"})

# new_product = Product(seller_id = seller.id)
# session.get(Seller,Product.seller_id)

class Seller(SQLModel,table=True):
    id: UUID = Field(sa_column=Column(
            postgresql.UUID,
            primary_key=True,
            default=uuid4
        ))
    name: str
    email: EmailStr
    password_hash : str
    address: str
    product: List[Product] = Relationship(back_populates="seller",sa_relationship_kwargs={"lazy":"selectin"})
