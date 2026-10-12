# Lecture 4.3 - POST: create a product (data as query parameters)
from typing import Any

from fastapi import FastAPI, HTTPException, status

app = FastAPI()

products = {
    1001: {"name": "Wireless Mouse", "price": 18.99, "stock": 42},
    1002: {"name": "Mechanical Keyboard", "price": 64.99, "stock": 18},
    1003: {"name": "USB-C Hub", "price": 29.99, "stock": 35},
    1004: {"name": "Laptop Stand", "price": 39.99, "stock": 12},
    1005: {"name": "Webcam", "price": 54.99, "stock": 25},
    1006: {"name": "Bluetooth Speaker", "price": 44.99, "stock": 30},
    1007: {"name": "External SSD", "price": 89.99, "stock": 10},
}


@app.get("/product")
def get_product(id: int) -> dict[str, Any]:
    if id not in products:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product with the given ID was not found!",
        )
    return products[id]


# Same URL as GET - different METHOD, so no clash
@app.post("/product")
def create_product(name: str, price: float, stock: int) -> dict[str, int]:
    # Validate product price
    if price <= 0:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Product price must be greater than zero.",
        )

    # Validate stock quantity
    if stock < 0:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Stock cannot be negative.",
        )

    # New id = biggest existing id + 1
    new_id = max(products.keys()) + 1

    products[new_id] = {"name": name, "price": price, "stock": stock}

    # Return the new id so the client can fetch the product later
    return {"id": new_id}
