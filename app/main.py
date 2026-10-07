from contextlib import asynccontextmanager
from typing import Any
from fastapi import FastAPI, HTTPException, status
from app.database.session import create_db_tables
from app.schema.models import ProductCreate, ProductRead, ProductUpdate
from app.database import Database

@asynccontextmanager
async def lifespan_handler(app: FastAPI):
    create_db_tables()        
    seed_products()
    yield

app = FastAPI(lifespan=lifespan_handler)


db = Database()
db.seed() 

def not_found() -> HTTPException:
    return HTTPException(status.HTTP_404_NOT_FOUND, "Given id doesn't exist!")

@app.get("/product",response_model=ProductRead)
def get_product(id: int) -> dict:

    product = db.get(id)
    # Check whether the requested product exists
    if product is None:
         not_found()

    return product

@app.post("/product")
def create_product(product: ProductCreate) -> dict[str, int]:
    return {"id": db.create(product)}

@app.patch("/product")
def patch_product(id : int, 
                  product: ProductUpdate,
                  )-> dict[str,Any]:
    
    if db.get(id) is None:
        raise not_found()
    return db.update(id, product)

@app.delete("/product")
def delete_product(id: int)-> dict[str,str]:

    if db.get(id) is None:
        raise not_found()
    db.delete(id)

    return {"detail":f"Deleted the product with id {id}"}