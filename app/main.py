from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, status
from fastapi.params import Depends
from typing import Any
from app.database.models import Product
from sqlmodel import Session

from app.database.session import create_db_tables, get_session
from app.schema.models import ProductCreate, ProductRead, ProductUpdate
# from app.database import Database

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_tables()
    yield
    # Cleanup code can go here if needed
    

# db = Database()
app = FastAPI(lifespan=lifespan)


@app.get("/product",response_model=ProductRead)
def get_product(id: int,session: Session = Depends(get_session)) -> dict:

    product = session.get(Product,id)
    # Check whether the requested product exists
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product with the given ID was not found!",
        )

    return product

@app.post("/product")
def create_product(data: ProductCreate, session: Session = Depends(get_session)) -> ProductRead:

    new_product = Product(**data.model_dump())
    session.add(new_product)
    session.commit()
    session.refresh(new_product)
    return new_product


@app.patch("/product")
def patch_product(id : int, 
                  body: ProductUpdate,
                  session: Session = Depends(get_session)
                  )-> dict[str,Any]:
    
    update = body.model_dump(exclude_none=True)

    if update is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Data to update the product is not provided!",
        )

    product = session.get(Product,id)
    product.sqlmodel_update(**update)
    session.commit()
    session.refresh(product)
    return product

@app.delete("/product")
def delete_product(id: int,session: Session = Depends(get_session))-> dict[str,str]:

     product = session.get(Product,id)
     if product is None:
         raise HTTPException(
             status_code=status.HTTP_404_NOT_FOUND,
             detail="Product with the given ID was not found!",
         )
     session.delete(product)
     session.commit()
     return {"detail":f"Deleted the product with id {id}"}