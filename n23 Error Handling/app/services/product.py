from uuid import UUID

from fastapi import HTTPException

from app.core.exception import EntityNotFound
from app.database.models import DeliveryPartner, Product, ProductStatus, Review, Seller, TagName
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.schema.product import ProductCreate, ProductUpdate
from app.services.delivery_partner import DeliveryPartnerService
from app.services.product_event import ProductEventService
from app.utils import decode_url_safe_token
from .base import BaseService

class ProductService(BaseService):
    def __init__(self, session: AsyncSession,partner_service: DeliveryPartnerService,event_service: ProductEventService):
        super().__init__(Product,session)
        self.partner_service = partner_service
        self.event_service = event_service

    async def get_product(self, id: UUID) -> Product | None:
        product =  await self._get(id)
        # if product is None:
        #     raise EntityNotFound()
        return {}

    async def add(self, product_create: ProductCreate,seller: Seller) -> Product:
        new_product = Product(
            **product_create.model_dump(),
            status=ProductStatus.placed,
            seller_id=seller.id,
            )
        partner = await self.partner_service.assign_product(new_product)
        product = await self._add(new_product)              
        
        # Create event while adding product 
        event = await self.event_service.add(
            product=product,
            location=seller.zip_code,
            status=ProductStatus.placed,
            description=f"assigned to {partner.name}"
            )
        product.timeline.append(event) 
        return product

    async def update(self, id: UUID, product_update: ProductUpdate,partner: DeliveryPartner) -> Product | None:
        product = await self._get(id)

        # Verify partner 
        if product.delivery_partner_id != partner.id:
            raise HTTPException(
                status_code=401,
                detail="Not Authorized"
            )
        update = product_update.model_dump(exclude_none=True)

        create_event = len(update) > 1 or not product_update.estimated_delivery

        if product_update.estimated_delivery:
            product.estimated_delivery = product_update.estimated_delivery

        update.pop("estimated_delivery",None)
        if create_event:
            await self.event_service.add(
                product=product,
                **update 
            )
    
        return await self._update(product)

    async def cancel(self,id: UUID,seller: Seller)-> Product:
        product = await self._get(id)

        if product.seller_id != seller.id:
            raise HTTPException(
                status_code=401,
                detail="Not Authorized"
            )

        # If product already cancelled then return that it is already cancelled and don't add in events now
        if product.status == ProductStatus.cancelled:
            raise HTTPException(
                status_code=400,
                detail="Product is already cancelled"
            )



        event = await self.event_service.add(
            product=product,
            status=ProductStatus.cancelled 
        )

        product.timeline.append(event)
        return product 
    
    async def delete(self, id: int) -> bool:
        return await self._delete(id)

    async def rate(self,token: str,rating: int, comment: str | None):
        token_data = decode_url_safe_token(token)

        if not token_data:
            raise HTTPException(
                 status_code=401,
                detail="Invalid Token"
            )

        # Get product from db
        product = await self._get(UUID(token_data["id"]))

        # Save Review for this product
        new_review = Review(
            rating=rating,
            comment=comment if comment else None,
            product_id = product.id
        )

        await self._add(new_review)

    # Add tag to an existing product 
    async def add_tag(self,id: UUID,tag_name: TagName) -> Product:

        product = await self._get(id)
        if product is None:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )
        tag = await tag_name.tag(self.session)

        # Check if tag already exists for this product
        if tag in product.tags:
            raise HTTPException(
                status_code=400,
                detail="Tag already exists for this product"
            )


        # Add tag to product
        product.tags.append(tag) 
        return await self._update(product)

    async def remove_tag(self,id: UUID,tag_name: TagName) -> Product:

        product = await self._get(id)
        if product is None:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )
        
        # Get tag from db
        tag = await tag_name.tag(self.session)

        if tag is None or tag not in product.tags:
            raise HTTPException(
                status_code=404,
                detail="Tag not found"
            )

        product.tags.remove(tag)

        return await self._update(product)