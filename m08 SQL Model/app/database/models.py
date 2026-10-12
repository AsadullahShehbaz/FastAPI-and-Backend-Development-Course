from datetime import datetime
from enum import Enum

from sqlmodel import Field, SQLModel


class ProductStatus(str, Enum):
    active = "active"
    low_stock = "low_stock"
    out_of_stock = "out_of_stock"
    discontinued = "discontinued"


# Inherit SQLModel + table=True  ->  this class becomes a TABLE
class Product(SQLModel, table=True):
    # Optional table name (default = lowercase class name)
    __tablename__ = "product"

    # default=None + primary_key=True -> the database assigns 1, 2, 3 ...
    id: int = Field(default=None, primary_key=True)

    name: str
    price: float = Field(gt=0, le=10_000)
    stock: int = Field(ge=0)
    warehouse: int
    status: ProductStatus
    warranty_until: datetime
