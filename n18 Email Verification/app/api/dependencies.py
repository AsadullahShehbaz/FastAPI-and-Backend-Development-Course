from typing import Annotated
from uuid import UUID
from fastapi import BackgroundTasks, HTTPException, status
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession 

from app.database.models import DeliveryPartner, ProductEvent, Seller
from app.database.redis import is_jti_blacklisted
from app.database.session import get_session

from app.services.delivery_partner import DeliveryPartnerService
from app.services.product import ProductService
from app.services.product_event import ProductEventService
from app.services.seller import SellerService

from app.core.security import oauth2_scheme_seller,oauth2_scheme_partner
from app.utils import decode_access_token


SessionDep = Annotated[AsyncSession,Depends(get_session)]

# Access token data 
async def _get_access_token(token: str)-> dict:
    data = decode_access_token(token)
  
    if data is None or await is_jti_blacklisted(data["jti"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid access token"
        )
    return data

async def get_seller_access_token(token: Annotated[str,Depends(oauth2_scheme_seller)],)-> dict:
    return await _get_access_token(token)

async def get_partner_access_token(token: Annotated[str,Depends(oauth2_scheme_partner)],)-> dict:
    return await _get_access_token(token)

# Get logged in seller 
async def get_current_seller(
        token_data : Annotated[dict,Depends(get_seller_access_token)],
        session: SessionDep
):
    seller = await session.get(Seller,UUID(token_data["user"]["id"]))
    if seller is None:
        raise HTTPException(status_code=401, detail="Not authorized")
    return seller

# Get logged in seller 
async def get_current_partner(
        token_data : Annotated[dict,Depends(get_partner_access_token)],
        session: SessionDep
):
    partner = await session.get(DeliveryPartner,UUID(token_data["user"]["id"]))
    if partner is None:
        raise HTTPException(status_code=401, detail="Not authorized")
    return partner

SellerDep = Annotated[Seller,Depends(get_current_seller)]
DeliveryPartnerDep = Annotated[DeliveryPartner,Depends(get_current_partner)]


def get_seller_service(session: SessionDep,tasks: BackgroundTasks):
    return SellerService(session,tasks)  

SellerServiceDep = Annotated[SellerService,Depends(get_seller_service)]

def get_partner_service(session: SessionDep,tasks: BackgroundTasks):
    return DeliveryPartnerService(session,tasks)  

DeliveryPartnerServiceDep = Annotated[DeliveryPartnerService,Depends(get_partner_service)]

def get_event_service(session: SessionDep,tasks: BackgroundTasks):
    return ProductEventService(session,tasks)  

ProductEventServiceDep = Annotated[ProductEventService,Depends(get_event_service)]


def get_product_service(session: SessionDep,partner_service: DeliveryPartnerServiceDep,event_service: ProductEventServiceDep):
    return ProductService(session,partner_service,event_service)  

ProductDep = Annotated[ProductService,Depends(get_product_service)]
