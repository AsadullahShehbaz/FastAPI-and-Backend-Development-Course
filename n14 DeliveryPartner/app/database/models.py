from datetime import datetime, timedelta, timezone
from uuid import uuid4,UUID
from typing import List
from enum import Enum
from sqlalchemy import ARRAY, INTEGER, Column
from sqlalchemy.dialects import postgresql
from sqlmodel import Relationship, SQLModel,Field
from pydantic import EmailStr

class ProductStatus(str,Enum):
    placed = "placed"
    in_transit = "in_transit"
    out_for_delivery = "out_for_delivery"
    delivered = "delivered"

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
    created_at: datetime = Field(
        sa_column=Column(
            postgresql.TIMESTAMP(timezone=True), # timestampz -> data type
            default= lambda: datetime.now(timezone.utc), # Actual Data Value
        )
    ) 
    status: ProductStatus
    estimated_delivery: datetime = Field(
        sa_column=Column(
            postgresql.TIMESTAMP(timezone=True), # timestampz -> data type
            default= lambda: datetime.now(timezone.utc) + timedelta(days=3), # Actual Data Value
        )
    ) 
    
    seller_id: UUID = Field(foreign_key="seller.id")
    delivery_partner_id: UUID = Field(foreign_key="delivery_partner.id")
    destination: int 
    seller: "Seller" = Relationship(back_populates="product",sa_relationship_kwargs={"lazy":"selectin"})
    delivery_partner: "DeliveryPartner" = Relationship(
        back_populates="products",
        sa_relationship_kwargs={"lazy": "selectin"},
    )

class User(SQLModel):
    name: str
    email: EmailStr
    password_hash: str


class Seller(User,table=True):
    __tablename__ = "seller"
    id: UUID = Field(sa_column=Column(
            postgresql.UUID,
            primary_key=True,
            default=uuid4
        ))

    product: List[Product] = Relationship(back_populates="seller",sa_relationship_kwargs={"lazy":"selectin"})

class DeliveryPartner(User, table=True):
    __tablename__ = "delivery_partner"
    id: UUID = Field(
        sa_column=Column(
            postgresql.UUID,
            default=uuid4,
            primary_key=True,
        )
    )
    serviceable_zip_codes: list[int] = Field(
        sa_column=Column(ARRAY(INTEGER))
    )
    max_handling_capacity: int

    created_at: datetime = Field(
        sa_column=Column(
            postgresql.TIMESTAMP(timezone=True), # timestampz -> data type
            default= lambda: datetime.now(timezone.utc), # Actual Data Value
        )
    ) 
    products: list[Product] = Relationship(
        back_populates="delivery_partner",
        sa_relationship_kwargs={"lazy": "selectin"},
    )

    # Get all products need to be delivered
    @property
    def active_products(self):
        return [product 
                for product in self.products
                if product.status != ProductStatus.delivered]

    # Current handling capacity of partner
    @property 
    def current_handling_capacity(self):
        return self.max_handling_capacity - len(self.active_products)
        
            