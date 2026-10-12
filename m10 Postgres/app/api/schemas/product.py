import random
from datetime import datetime

from pydantic import BaseModel, Field

from app.database.models import ProductStatus


def random_warehouse() -> int:
    return random.randint(1, 5)


class BaseProduct(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    price: float = Field(gt=0, le=10_000)
    stock: int = Field(ge=0)
    warehouse: int = Field(default_factory=random_warehouse, ge=1, le=5)


class ProductRead(BaseProduct):
    id: int
    status: ProductStatus
    warranty_until: datetime


class ProductCreate(BaseProduct):
    pass


class ProductUpdate(BaseModel):
    price: float | None = Field(default=None, gt=0, le=10_000)
    stock: int | None = Field(default=None, ge=0)
    status: ProductStatus | None = Field(default=None)
    warranty_until: datetime | None = Field(default=None)
