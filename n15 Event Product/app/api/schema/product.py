from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field

from app.api.schema.seller import SellerRead
from app.database.models import ProductEvent, ProductStatus

class BaseProduct(BaseModel):
     name: str = Field(
          description="Product title",
          min_length=3,
          max_length=100
     )
     price: float = Field(
          description="Price is USD",
          gt=0
     )
     stock: int = Field(
          description="Unit available in warehouse",
          gt=0
     )
     destination: int = Field(description="Zip Code of Product Destination")
class ProductCreate(BaseProduct):
     pass

class ProductRead(BaseProduct):
     id: UUID
     status: ProductStatus
     estimated_delivery: datetime
     seller: SellerRead
     timeline: list[ProductEvent]

class ProductUpdate(BaseModel):
     status: ProductStatus | None = Field(default=None)
     location: int | None = Field(default=None)
     description: str | None = Field(default=None)
     estimated_delivery: datetime | None = Field(default=None)

