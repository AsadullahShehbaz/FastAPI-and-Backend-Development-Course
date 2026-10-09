from fastapi import HTTPException, status
from fastapi import APIRouter

from app.schema.models import ProductCreate, ProductRead, ProductUpdate
from app.database.session import SessionDep
from app.database.models import Product
from app.schema.models import ProductRead

router = APIRouter()

@router.get("/product",response_model=ProductRead)
async def get_product(id: int,session: SessionDep) -> dict:

    product = await session.get(Product,id)
    # Check whether the requested product exists
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product with the given ID was not found!",
        )

    return product

@router.post("/product")
async def create_product(data: ProductCreate, session: SessionDep) -> ProductRead:

    new_product = Product(**data.model_dump())
    session.add(new_product)
    await session.commit()
    await session.refresh(new_product)
    return new_product


@router.patch("/product")
async def patch_product(id : int, 
                  body: ProductUpdate,
                  session: SessionDep
                  )-> ProductRead:
    
    update = body.model_dump(exclude_none=True)

    if not update:
        raise HTTPException(
            status_code=400,
            detail="Data to update the product is not provided!",
        )

    product = await session.get(Product,id)
    product.sqlmodel_update(update)
    await session.commit()
    await session.refresh(product)
    return product

@router.delete("/product")
async def delete_product(id: int,session: SessionDep)-> dict[str,str]:

     product = await session.get(Product,id)
     if product is None:
         raise HTTPException(
             status_code=status.HTTP_404_NOT_FOUND,
             detail="Product with the given ID was not found!",
         )
     await session.delete(product)
     await session.commit()
     return {"detail":f"Deleted the product with id {id}"}