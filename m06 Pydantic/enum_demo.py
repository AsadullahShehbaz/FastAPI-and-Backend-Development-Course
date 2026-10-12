# Lecture 6.3 - Enums: restrict a value to a fixed set
from enum import Enum

from fastapi import FastAPI

app = FastAPI()


# Inherit "str" first so each value is a real string
class ProductStatus(str, Enum):
    active = "active"
    low_stock = "low_stock"
    out_of_stock = "out_of_stock"
    discontinued = "discontinued"


products = {
    1001: {"name": "Wireless Mouse", "price": 18.99, "stock": 42, "status": "active"},
}


# dict[str, str]  -> accepts ANY string, even "nowhere"
# dict[str, ProductStatus] -> only the four allowed values
@app.put("/product/status")
def set_status(id: int, body: dict[str, ProductStatus]) -> dict:
    products[id]["status"] = body["status"]
    return products[id]


print(ProductStatus.active)          # ProductStatus.active
print(ProductStatus.active.value)    # active
