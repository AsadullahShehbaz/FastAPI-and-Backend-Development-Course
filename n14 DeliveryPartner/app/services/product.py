from app.database.models import Product, ProductStatus, Seller
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.schema.product import ProductCreate
from app.services.delivery_partner import DeliveryPartnerService
from .base import BaseService

class ProductService(BaseService):
    def __init__(self, session: AsyncSession,partner_service: DeliveryPartnerService):
        super().__init__(Product,session)
        self.partner_service = partner_service

    async def get(self, id: int) -> Product | None:
        return await self._get(id)

    async def add(self, product_create: ProductCreate,seller: Seller) -> Product:
        new_product = Product(
            **product_create.model_dump(),
            status=ProductStatus.placed,
            seller_id=seller.id,
            )
        await self.partner_service.assign_product(new_product)
        return await self._add(new_product)              

    async def update(self, id: int, product_update: dict) -> Product | None:
        return await self._update(id,product_update)
        
    async def delete(self, id: int) -> bool:
       
        return await self._delete(id)
        