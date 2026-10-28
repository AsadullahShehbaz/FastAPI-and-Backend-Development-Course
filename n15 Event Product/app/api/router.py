from fastapi import APIRouter
from app.api.routers import seller,product,delivery_partner

router = APIRouter()

router.include_router(seller.router)
router.include_router(product.router)
router.include_router(delivery_partner.router)