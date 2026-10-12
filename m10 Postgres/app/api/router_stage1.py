# Lecture 10.3 (STAGE 1, for teaching only - not included by main.py)
# Endpoints made async, still talking to the session directly.
# Notice the repeated add -> commit -> refresh work in every endpoint.
from datetime import datetime, timedelta

from fastapi import APIRouter, HTTPException, status

from app.api.dependencies import SessionDep
from app.database.models import Product, ProductStatus

from .schemas.product import ProductCreate

router = APIRouter()


@router.get("/product")
async def get_product(id: int, session: SessionDep):
    product = await session.get(Product, id)              # await: returns a coroutine
    if product is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Given id doesn't exist!")
    return product


@router.post("/product")
async def submit_product(product: ProductCreate, session: SessionDep) -> dict[str, int]:
    new_product = Product(
        **product.model_dump(),
        status=ProductStatus.active,
        warranty_until=datetime.now() + timedelta(days=365),
    )
    session.add(new_product)                 # NO await: add() returns None
    await session.commit()                   # await
    await session.refresh(new_product)       # await
    return {"id": new_product.id}
