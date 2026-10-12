# Lecture 6.1 - Why Pydantic?  dict body (no validation) vs BaseModel
from typing import Any

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

products = {
    1001: {"name": "Wireless Mouse", "price": 18.99, "stock": 42},
    1002: {"name": "Mechanical Keyboard", "price": 64.99, "stock": 18},
}


# A schema = a class that inherits BaseModel + typed class variables
class Product(BaseModel):
    name: str
    price: float
    stock: int


# BEFORE: plain dict body -> "price": "cheap" is accepted, nothing validated
@app.post("/product/unsafe")
def create_product_unsafe(data: dict[str, Any]) -> dict[str, int]:
    new_id = max(products.keys()) + 1
    products[new_id] = data
    return {"id": new_id}


# AFTER: Pydantic model -> FastAPI validates every field's type for us
@app.post("/product")
def create_product(product: Product) -> dict[str, int]:
    if product.price <= 0:                      # dot access, like any object
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Product price must be greater than zero.",
        )

    new_id = max(products.keys()) + 1
    products[new_id] = {
        "name": product.name,
        "price": product.price,
        "stock": product.stock,
    }
    return {"id": new_id}
