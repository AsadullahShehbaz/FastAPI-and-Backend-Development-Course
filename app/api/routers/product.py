from fastapi import HTTPException, status
from fastapi import APIRouter

from app.api.schema.models import ProductCreate, ProductRead, ProductUpdate
from app.database.session import ServiceDep
from app.database.models import Product
from app.api.schema.models import ProductRead

router = APIRouter(prefix='/product',tags=["Product"])

@router.get("/",response_model=ProductRead)
async def get_product(id: int,service: ServiceDep) -> dict:

    product = await service.get(id)
    # Check whether the requested product exists
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product with the given ID was not found!",
        )

    return product

@router.post("/")
async def create_product(product: ProductCreate, service: ServiceDep) -> ProductRead:
    return await service.add(product)

@router.patch("/")
async def patch_product(id : int, 
                  body: ProductUpdate,
                  service: ServiceDep
                  )-> ProductRead:
    
    update = body.model_dump(exclude_none=True)

    if not update:
        raise HTTPException(
            status_code=400,
            detail="Data to update the product is not provided!",
        )
    product = await service.update(id,update)
    if product is None:
        raise HTTPException(
                    status_code=404,
                    detail="Product does n't exist with this ID!",
                )
    return product

@router.delete("/")
async def delete_product(id: int,service: ServiceDep)-> dict[str,str]:

    
     if not await service.delete(id):
         raise HTTPException(
             status_code=status.HTTP_404_NOT_FOUND,
             detail="Product with the given ID was not found!",
         )
     
     return {"detail":f"Deleted the product with id {id}"}