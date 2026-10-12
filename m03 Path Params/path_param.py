# Lecture 3.3 - Path parameters
from typing import Any

from fastapi import FastAPI

app = FastAPI()


#                path parameter
@app.get("/product/{id}")
def get_product(id: int) -> dict[str, Any]:
    #                ^ type hint = automatic validation
    return {
        "id": id,
        "name": "Wireless Mouse",
        "price": 18.99,
        "stock": 42,
    }
