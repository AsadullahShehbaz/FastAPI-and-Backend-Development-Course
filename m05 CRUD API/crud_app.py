# Module 5 - Complete CRUD API for products (dict datastore)
# Run:  fastapi dev m05/crud_app.py
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


def get_or_404(id: int) -> dict[str, Any]:
    if id not in products:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product with the given ID was not found!",
        )
    return products[id]


### READ
@app.get("/product")
def get_product(id: int) -> dict[str, Any]:
    return get_or_404(id)


### CREATE
@app.post("/product")
def create_product(name: str, price: float, stock: int) -> dict[str, int]:
    if price <= 0:
        raise HTTPException(status.HTTP_406_NOT_ACCEPTABLE, "Price must be > 0")
    if stock < 0:
        raise HTTPException(status.HTTP_406_NOT_ACCEPTABLE, "Stock cannot be negative")

    new_id = max(products.keys()) + 1
    products[new_id] = {"name": name, "price": price, "stock": stock}
    return {"id": new_id}


### UPDATE (replace everything) - every field is required
@app.put("/product")
def replace_product(
    id: int, name: str, price: float, stock: int,
) -> dict[str, Any]:
    get_or_404(id)                       # must exist first
    products[id] = {"name": name, "price": price, "stock": stock}
    return products[id]


### UPDATE (partial) - body holds only the fields to change
@app.patch("/product")
def update_product(id: int, body: dict[str, Any]) -> dict[str, Any]:
    product = get_or_404(id)
    product.update(body)                 # only the given keys change
    return product


### DELETE
@app.delete("/product")
def delete_product(id: int) -> dict[str, str]:
    get_or_404(id)                       # pop() would raise KeyError otherwise
    products.pop(id)
    return {"detail": f"Product with id #{id} is deleted!"}
