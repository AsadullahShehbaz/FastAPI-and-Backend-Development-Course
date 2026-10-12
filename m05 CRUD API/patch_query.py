# Lecture 5.2 (version 1) - PATCH with optional query parameters
from typing import Any

from fastapi import FastAPI, HTTPException, status

app = FastAPI()

products = {
    1001: {"name": "Wireless Mouse", "price": 18.99, "stock": 42},
    1002: {"name": "Mechanical Keyboard", "price": 64.99, "stock": 18},
}


@app.patch("/product")
def patch_product(
    id: int,                         # required
    name: str | None = None,         # optional
    price: float | None = None,      # optional
    stock: int | None = None,        # optional
) -> dict[str, Any]:
    if id not in products:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Product not found")

    product = products[id]

    # Separate ifs (NOT elif): several fields can arrive together.
    # Use "is not None" - "if stock:" would wrongly IGNORE stock=0 !
    if name is not None:
        product["name"] = name
    if price is not None:
        product["price"] = price
    if stock is not None:
        product["stock"] = stock

    products[id] = product
    return product
