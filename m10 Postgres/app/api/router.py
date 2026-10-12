from fastapi import APIRouter, HTTPException, status

from .dependencies import ServiceDep
from .schemas.product import ProductCreate, ProductRead, ProductUpdate

# The router groups the endpoints; prefix + tags are applied to all of them
router = APIRouter(prefix="/product", tags=["Product"])


def not_found() -> HTTPException:
    return HTTPException(status.HTTP_404_NOT_FOUND, "Given id doesn't exist!")


@router.get("/", response_model=ProductRead)
async def get_product(id: int, service: ServiceDep):
    product = await service.get(id)
    if product is None:
        raise not_found()
    return product


@router.post("/")
async def create_product(product: ProductCreate, service: ServiceDep) -> ProductRead:
    # return type = schema, so response_model is not needed
    return await service.add(product)


@router.patch("/", response_model=ProductRead)
async def update_product(id: int, product_update: ProductUpdate, service: ServiceDep):
    update = product_update.model_dump(exclude_none=True)
    if not update:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "No data provided to update")

    # pass the FILTERED dict, never the whole schema (None would overwrite data)
    product = await service.update(id, update)
    if product is None:
        raise not_found()
    return product


@router.delete("/")
async def delete_product(id: int, service: ServiceDep) -> dict[str, str]:
    if not await service.delete(id):
        raise not_found()
    return {"detail": f"Product with id #{id} is deleted!"}
