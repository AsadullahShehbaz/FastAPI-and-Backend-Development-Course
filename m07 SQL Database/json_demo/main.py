# Lecture 7.1 - API that saves to products.json
# Run (from the m07 folder):  fastapi dev json_demo/main.py
from typing import Any

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

from .database import products, save


class ProductCreate(BaseModel):
    name: str
    price: float
    stock: int


app = FastAPI()


@app.get("/product")
def get_product(id: int) -> dict[str, Any]:
    if id not in products:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Given id doesn't exist!")
    return products[id]


@app.post("/product")
def create_product(product: ProductCreate) -> dict[str, int]:
    new_id = max(products.keys()) + 1
    products[new_id] = {
        "id": new_id,                  # the id lives INSIDE the value now
        **product.model_dump(),
    }
    save()                             # persist after every change
    return {"id": new_id}
