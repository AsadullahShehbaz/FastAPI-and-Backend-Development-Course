from fastapi import HTTPException, status
from fastapi import APIRouter
from sqlalchemy import update

from app.api.schema.product import ProductCreate, ProductRead, ProductUpdate
from app.api.dependencies import DeliveryPartnerDep, ProductDep, SellerDep
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
                  partner : DeliveryPartnerDep,
                  service: ProductDep 
                  )-> ProductRead:

    if not body.model_dump(exclude_none=True):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "No data provided to update")
    return await service.update(id, body,partner)

@router.get("/",response_model=ProductRead)
async def cancel_product(id: UUID, seller : SellerDep,service: ProductDep ):
    return await service.cancel(id,seller)


