import datetime
from app.schema.models import ProductStatus
from sqlmodel import SQLModel, Field  # type: ignore[import-not-found]

class Product(SQLModel, table=True):
    __tablename__ = "product"
    id: int = Field(default=None, primary_key=True)
    name: str
    price: float = Field(gt=0, le=10_000)
    stock: int = Field(ge=0)
    warehouse: int
    status: ProductStatus
    warranty_until: datetime