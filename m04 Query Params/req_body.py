# Lecture 4.4 - Request body (plain dict) - and why it is not enough
from typing import Any

from fastapi import FastAPI, HTTPException, status

app = FastAPI()

products = {
    1001: {"name": "Wireless Mouse", "price": 18.99, "stock": 42},
    1002: {"name": "Mechanical Keyboard", "price": 64.99, "stock": 18},
    1003: {"name": "USB-C Hub", "price": 29.99, "stock": 35},
}


@app.get("/product")
def get_product(id: int) -> dict[str, Any]:
    if id not in products:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product with the given ID was not found!",
        )
    return products[id]


# A dict-typed argument tells FastAPI: "read this from the request BODY"
@app.post("/product")
def create_product(data: dict[str, Any]) -> dict[str, int]:
    name = data["name"]          # KeyError (500!) if the client forgot "name"
    price = data["price"]
    stock = data["stock"]

    if price <= 0:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Product price must be greater than zero.",
        )

    new_id = max(products.keys()) + 1
    products[new_id] = {"name": name, "price": price, "stock": stock}
    return {"id": new_id}


# Query parameter + request body in ONE endpoint
# (different URL here only so both demos can live in one file)
@app.post("/product/mixed")
def create_product_mixed(price: float, data: dict[str, str]) -> dict[str, int]:
    name = data["name"]                 # from the body
    new_id = max(products.keys()) + 1
    products[new_id] = {"name": name, "price": price, "stock": 0}
    return {"id": new_id}
