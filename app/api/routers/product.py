from fastapi import HTTPException, status
from fastapi import APIRouter
from sqlalchemy import update

from app.api.schema.models import ProductCreate, ProductRead, ProductUpdate
from app.api.dependencies import ServiceDep 
from app.api.schema.models import ProductRead

router = APIRouter(prefix="/product/v1", tags=["Product"])

@router.get("/{id}",response_model=ProductRead)
async def get_product(id: int,service: ServiceDep ) -> dict:

    product = await service.get(id)
    # Check whether the requested product exists
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product with the given ID was not found!",
        )

    return product

@router.post("/")
async def create_product(data: ProductCreate, service: ServiceDep ) -> ProductRead:

    return await service.add(data)


@router.patch("/")
async def patch_product(id : int, 
                  body: ProductUpdate,
                  service: ServiceDep 
                  )-> ProductRead:

    update = body.model_dump(exclude_unset=True)
    if not update:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "No data provided to update")
    product =await service.update(id, update)
    return product

@router.delete("/")
async def delete_product(id: int,service: ServiceDep )-> dict[str,str]:

    deleted = await service.delete(id)
    return {"message": "Product deleted successfully"} if deleted else {"message": "Product not found"}