from typing import Any
from fastapi import FastAPI, HTTPException, status
from app.schema.models import ProductCreate, ProductRead, ProductStatus, ProductUpdate

app = FastAPI()


@app.get("/product",response_model=ProductRead)
def get_product(id: int) -> dict:

    # Check whether the requested product exists
    if id not in products:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product with the given ID was not found!",
        )

    return products[id]

@app.post("/product")
def create_product(data: ProductCreate) -> dict[str,Any]:

    new_id = max(products.keys()) + 1

    products[new_id] = {
         **data.model_dump(),
         "status":ProductStatus.active
    }

    return {"id":new_id}

@app.put("/product")
def replace_product(id : int, name: str, price: float , stock : int)-> dict[str,Any]:

    if id not in products:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product with the given ID was not found!",
            )
    product = products[id]

    product = {
        "name": name,
        "price":price,
        "stock":stock
    }

    products[id] = product

    return products[id]

@app.patch("/product")
def patch_product(id : int, 
                  body: ProductUpdate,
                  )-> dict[str,Any]:
    
    data = body.model_dump(exclude_unset=True)

    if not data:
         raise HTTPException(
              status_code=400,
              detail="No data provided to update"
         )

    products[id].update(data)
    return products[id]

@app.delete("/product")
def delete_product(id: int)-> dict[str,str]:

     products.pop(id)

     return {"detail":f"Deleted the product with id {id}"}