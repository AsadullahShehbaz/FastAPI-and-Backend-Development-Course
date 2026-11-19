from uuid import UUID

from fastapi import HTTPException,status
from sqlalchemy import Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import any_,select
from app.database.models import DeliveryPartner, Location,Product
from app.api.schema.delivery_partner import DeliveryPartnerCreate, DeliveryPartnerUpdate
from .user import UserService

class DeliveryPartnerService(UserService):
    def __init__(self,session: AsyncSession):
        super().__init__(DeliveryPartner,session)

    async def add(self,data: DeliveryPartnerCreate)-> DeliveryPartner:
        partner: DeliveryPartner = await self._add_user(data.model_dump(exclude={"serviceable_zip_codes"}),router_prefix="partner")

        for zip_code in data.serviceable_zip_codes: 

            # Get location from database related to this zip_code 
            location = await self.session.get(Location,zip_code)

            if location is None:
                location = Location(zip_code=zip_code)

            # Append zip code to the partner 
            partner.serviceable_locations.append(location)

    async def login(self,email , password)->str:
      return await self._generate_token(email,password)

    async def update(self,id:UUID, data: DeliveryPartnerUpdate)-> DeliveryPartner:
        return await self._update(id,data.model_dump(exclude_none=True))

    async def get_partner_by_zipcode(self,zipcode:int)-> Sequence[DeliveryPartner]:
        return ( await self.session.scalars(
            select(DeliveryPartner).join(DeliveryPartner.serviceable_locations).where(Location.zip_code==zipcode)
            )
            ).all()
    
    # Assign product to specific partner 
    async def assign_product(self,product: Product):
        eligible_partners = await self.get_partner_by_zipcode(product.destination)

        for partner in eligible_partners:
            if partner.current_handling_capacity > 0:
                partner.products.append(product)
                return partner 

        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="No delivery partner available"
        )
        
   