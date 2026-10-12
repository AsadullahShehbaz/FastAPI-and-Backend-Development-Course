# Lecture 4.5 - Path parameter + query parameter together
from typing import Any

from fastapi import FastAPI, HTTPException, status

app = FastAPI()

products = {
    1001: {"name": "Wireless Mouse", "price": 18.99, "stock": 42},
    1002: {"name": "Mechanical Keyboard", "price": 64.99, "stock": 18},
    1003: {"name": "USB-C Hub", "price": 29.99, "stock": 35},
    1004: {"name": "Laptop Stand", "price": 39.99, "stock": 12},
    1005: {"name": "Webcam", "price": 54.99, "stock": 25},
}


#   {field} -> path parameter      id -> query parameter
@app.get("/product/{field}")
def get_product_field(field: str, id: int) -> dict[str, Any]:
    if id not in products:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Product not found")
    if field not in products[id]:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"Unknown field '{field}'")

    return {field: products[id][field]}
