# Lecture 7.7 - Use the Database class inside the API
# Run (from the m07 folder):  fastapi dev app/main.py
from fastapi import FastAPI, HTTPException, status

from .database import Database
from .schemas import ProductCreate, ProductRead, ProductUpdate

app = FastAPI()

db = Database()          # one shared instance (connects + creates table)
db.seed()                # load the 7 starter products the first time


def not_found() -> HTTPException:
    return HTTPException(status.HTTP_404_NOT_FOUND, "Given id doesn't exist!")


@app.get("/product", response_model=ProductRead)
def get_product(id: int):
    product = db.get(id)           # None replaces "id not in dict"
    if product is None:
        raise not_found()
    return product


@app.post("/product")
def create_product(product: ProductCreate) -> dict[str, int]:
    return {"id": db.create(product)}


@app.patch("/product", response_model=ProductRead)
def update_product(id: int, product: ProductUpdate):
    if db.get(id) is None:
        raise not_found()
    return db.update(id, product)


@app.delete("/product")
def delete_product(id: int) -> dict[str, str]:
    if db.get(id) is None:
        raise not_found()
    db.delete(id)
    return {"detail": f"Product with id #{id} is deleted"}
