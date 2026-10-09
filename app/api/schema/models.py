from enum import Enum
import random
from pydantic import BaseModel, Field

def random_warehouse() -> int:
     return random.randint(1,5)

class ProductStatus(str,Enum):
     active = "active"
     low_stock = "low_stock"
     out_of_stock = "out_of_stock"

class BaseProduct(BaseModel):
     name: str = Field(
          description="Product title",
          min_length=3,
          max_length=100
     )
     price: float = Field(
          description="Price is USD",
          gt=0,
          le=1000
     )
     stock: int = Field(
          description="Unit available in warehouse",
          gt=0
     )

     status: ProductStatus = Field(
          default=ProductStatus.active,
          description="Current stock status of the product"
     )

class ProductCreate(BaseProduct):
     pass

class ProductRead(BaseProduct):
     pass 

class ProductUpdate(BaseModel):
     name: str | None = Field(
               default=None,
               description="Product title",
               min_length=3,
               max_length=100
          )
     price: float | None = Field(
          default=None,
          description="Price is USD",
          gt=0,
          le=1000
     )
     stock: int | None = Field(
          default=None,
          description="Unit available in warehouse",
          gt=0
     )
     status: ProductStatus | None = Field(
          default=None,
          description="Current stock status of the product"
     )
