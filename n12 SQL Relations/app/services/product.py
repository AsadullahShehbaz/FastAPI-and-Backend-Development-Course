from app.database.models import Product, Seller
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.schema.product import ProductCreate

class ProductService:
    def __init__(self, session: AsyncSession):
        # the service receives the session and keeps it
        self.session = session

    async def get(self, id: int) -> Product | None:
        return await self.session.get(Product, id)

    async def add(self, product_create: ProductCreate,seller: Seller) -> Product:
        new_product = Product(**product_create.model_dump(),seller_id=seller.id)
        self.session.add(new_product)              
        await self.session.commit()
        await self.session.refresh(new_product)
        return new_product

    async def update(self, id: int, product_update: dict) -> Product | None:
        product = await self.get(id)
        if product is None:
            return None
        product.sqlmodel_update(product_update)    
        self.session.add(product)
        await self.session.commit()
        await self.session.refresh(product)
        return product

    async def delete(self, id: int) -> bool:
        product = await self.get(id)
        if product is None:
            return False
        await self.session.delete(product)
        await self.session.commit()
        return True