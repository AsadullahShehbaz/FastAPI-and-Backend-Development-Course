# Lecture 8.6 - ONE SQLModel used as BOTH the API schema and the table
#
# This file REPLACES database/models.py + schemas.py. Do not import it together
# with database/models.py - both would define a table named "product".
from datetime import datetime
from enum import Enum

from sqlmodel import Field, SQLModel


class ProductStatus(str, Enum):
    active = "active"
    low_stock = "low_stock"
    out_of_stock = "out_of_stock"
    discontinued = "discontinued"


# Base: NO table=True (inheritance only, no table created)
class BaseProduct(SQLModel):
    name: str = Field(min_length=3, max_length=100)
    price: float = Field(gt=0, le=10_000)
    stock: int = Field(ge=0)
    warehouse: int = Field(ge=1, le=5)


# table=True is the "switch" that makes THIS class a table
class Product(BaseProduct, table=True):
    id: int = Field(default=None, primary_key=True)
    status: ProductStatus
    warranty_until: datetime


# These stay plain schemas (no table)
class ProductCreate(BaseProduct):
    pass
