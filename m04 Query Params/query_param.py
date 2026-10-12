# Lecture 4.1 - Query parameters:  /product?id=1002
from typing import Any

from fastapi import FastAPI

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


# "id" is NOT in the path -> FastAPI treats it as a query parameter
# "int | None = None" -> optional
@app.get("/product")
def get_product(id: int | None = None) -> dict[str, Any]:
    # No id given -> return the latest product
    if id is None:
        id = max(products.keys())
        return products[id]

    if id not in products:
        return {"detail": "Given id doesn't exist!"}
    return products[id]
