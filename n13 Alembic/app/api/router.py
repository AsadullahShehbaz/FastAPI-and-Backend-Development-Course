from fastapi import APIRouter
from app.api.routers import seller,product

router = APIRouter()

router.include_router(seller.router)
router.include_router(product.router)