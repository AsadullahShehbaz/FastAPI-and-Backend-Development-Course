from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, status
from fastapi.params import Depends
from sqlmodel import Session
from typing import Any
from app.database.models import Product

from app.database.session import SessionDep, create_db_tables, get_session
from app.schema.models import ProductCreate, ProductRead, ProductUpdate
# from app.database import Database

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_tables()
    yield
    # Cleanup code can go here if needed
    

# db = Database()
app = FastAPI(lifespan=lifespan)


@app.get("/product")
async def get_product(id: int,session: SessionDep) -> ProductRead: # type: ignore

    product = session.get(Product,id)
    # Check whether the requested product exists
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product with the given ID was not found!",
        )

    return product

@app.post("/product")
def create_product(data: ProductCreate, session: SessionDep) -> ProductRead:

    new_product = Product(**data.model_dump())
    session.add(new_product)
    session.commit()
    session.refresh(new_product)
    return new_product


@app.patch("/product")
def patch_product(id : int, 
                  data: ProductUpdate,
                  session: SessionDep
                  )-> ProductRead:
    
    update = data.model_dump(exclude_none=True)
    if not update:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No fields provided for update!",
        )

    product = session.get(Product,id)
    product.sqlmodel_update(update)

    session.add(product)
    session.commit()
    session.refresh(product)
    return product


@app.delete("/product")
def delete_product(id: int, session: SessionDep)-> dict[str,str]:

     product = session.get(Product,id)
     if product is None:
         raise HTTPException(
             status_code=status.HTTP_404_NOT_FOUND,
             detail="Product with the given ID was not found!",
         )
     session.delete(product)
     session.commit()
     return {"detail":f"Deleted the product with id {id}"}