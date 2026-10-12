from pydantic import BaseModel, Field


class BaseProduct(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    price: float = Field(gt=0, le=10_000)
    stock: int = Field(ge=0)


class ProductRead(BaseProduct):
    id: int


class ProductCreate(BaseProduct):
    pass


class ProductUpdate(BaseModel):
    price: float | None = Field(default=None, gt=0, le=10_000)
    stock: int | None = Field(default=None, ge=0)
