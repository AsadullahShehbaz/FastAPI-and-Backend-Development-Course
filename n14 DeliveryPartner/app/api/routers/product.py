from fastapi import HTTPException, status
from fastapi import APIRouter
from sqlalchemy import update

from app.api.schema.product import ProductCreate, ProductRead, ProductUpdate
from app.api.dependencies import ProductDep, SellerDep
from app.api.schema.product import ProductRead
from uuid import UUID
router = APIRouter(prefix="/product/v1", tags=["Product"])

@router.get("/{id}",response_model=ProductRead)
async def get_product(id: UUID, _ : SellerDep,service: ProductDep ) -> dict:

    product = await service.get(id)
    # Check whether the requested product exists
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product with the given ID was not found!",
        )

    return product

@router.post("/")
async def create_product(data: ProductCreate, seller : SellerDep, service: ProductDep ) -> ProductRead:

    return await service.add(data,seller)


@router.patch("/")
async def patch_product(id : UUID, 
                  body: ProductUpdate,
                   _ : SellerDep,
                  service: ProductDep 
                  )-> ProductRead:

    update = body.model_dump(exclude_unset=True)
    if not update:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "No data provided to update")
    product =await service.update(id, update)
    return product

@router.delete("/")
async def delete_product(id: int, _ : SellerDep,service: ProductDep )-> dict[str,str]:

    deleted = await service.delete(id)
    return {"message": "Product deleted successfully"} if deleted else {"message": "Product not found"}