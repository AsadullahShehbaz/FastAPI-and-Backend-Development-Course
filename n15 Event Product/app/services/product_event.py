from app.database.models import ProductEvent,Product,ProductStatus
from sqlalchemy.ext.asyncio import AsyncSession
from .base import BaseService

class ProductEventService(BaseService):
    """
    A service that creates timeline events. Client can pass only what changed, and the service fills in the rest from the Product's latest event.
    """
    def __init__(self, session: AsyncSession):
        super().__init__(ProductEvent,session)

    def _get_latest_timeline(self,product: Product)-> ProductEvent:

        if not product.timeline:
            return None
        timeline = product.timeline
        return max(timeline,key=lambda event: event.created_at)


    def _generate_description(self,status: ProductStatus,location: int)->str:
        match status:
            case ProductStatus.placed:
                return "assigned delivery partner"
            case ProductStatus.delivered:
                 return "successfully delivered"
            case ProductStatus.cancelled:
                return "cancelled by seller"
            case _:
                return f"scanned at {location}"
    
    async def add(self,product: Product,location: int | None = None, status: ProductStatus | None = None ,description: str | None = None):

        latest_event = self._get_latest_timeline(product)

        if latest_event is not None:
            location = location if location is not None else latest_event.location
            status = status if status is not None else latest_event.status
        
        # Initialize product event class object 
        new_event = ProductEvent(
            location = location,
            status = status,
            description = (description if description is not None else self._generate_description(status,location)),
            product_id = product.id
        )
        return await self._add(new_event)


   
      