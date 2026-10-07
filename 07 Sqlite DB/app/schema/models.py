from enum import Enum
import random
from pydantic import BaseModel, Field

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
     warehouse: int | None = Field(
          default=None,
          description="Warehouse code (1-5)",
          #   default=1,
          # default_factory=random_warehouse      
     )