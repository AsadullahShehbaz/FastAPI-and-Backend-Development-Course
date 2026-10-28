from fastapi import BackgroundTasks

from app.database.models import ProductEvent,Product,ProductStatus
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.notification import NotificationService

from .base import BaseService

class ProductEventService(BaseService):
    """
    A service that creates timeline events. Client can pass only what changed, and the service fills in the rest from the Product's latest event.
    """
    def __init__(self, session: AsyncSession,tasks: BackgroundTasks):
        super().__init__(ProductEvent,session)
        self.notification_service = NotificationService(tasks)
       

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
    async def _notify(self,product: Product,status: ProductStatus):

        subject,context,template_name=" ",{ }," "
        match status:
            case ProductStatus.placed:
                    subject="Your order is shipped"
                    context["seller"] = product.seller.name
                    context["partner"] = product.delivery_partner.name
                    template_name="mail-placed.html"
            
            case ProductStatus.out_for_delivery:
                subject="Your order is arriving"
                context["seller"] = product.seller.name
                context["partner"] = product.delivery_partner.name
                template_name="mail-out-for-delivery.html"

        await self.notification_service.send_mail_with_template(
            recipient=[product.client_contact_email],
            subject=subject,
            context=context,
            template_name=template_name
        )

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

        await self._notify(product,status)
        return await self._add(new_event)


   
      