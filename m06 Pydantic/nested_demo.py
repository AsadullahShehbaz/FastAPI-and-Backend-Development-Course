# Lecture 6.6 (tip 3) - Nested models
from pydantic import BaseModel, Field


class Supplier(BaseModel):
    name: str
    email: str
    country: str = "PK"


class ProductCreate(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    price: float = Field(gt=0)
    stock: int = Field(ge=0)
    supplier: Supplier                 # a model INSIDE a model
    tags: list[str] = []               # a list of strings


example = ProductCreate(
    name="Wireless Mouse",
    price=18.99,
    stock=42,
    supplier={"name": "Asadullah AI", "email": "asadullah@gmail.pk"},
    tags=["mouse", "wireless"],
)
print(example.model_dump())
