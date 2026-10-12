from typing import Annotated
from fastapi import HTTPException, status
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession 

from app.database.models import Seller
from app.database.redis import is_jti_blacklisted
from app.database.session import get_session

from app.services.product import ProductService
from app.services.seller import SellerService

from app.core.security import oauth2_scheme 
from app.utils import decode_access_token


SessionDep = Annotated[AsyncSession,Depends(get_session)]

def get_product_service(session: SessionDep):
    return ProductService(session)  

# Access token data 
async def get_access_token(token: Annotated[str,Depends(oauth2_scheme)],)-> dict:
    data = decode_access_token(token)
  
    if data is None or await is_jti_blacklisted(data["jti"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid access token"
        )
    return data

# Get logged in seller 
async def get_current_seller(
        token_data : Annotated[dict,Depends(get_access_token)],
        session: SessionDep
):
    return await session.get(Seller,token_data["user"]["id"])

SellerDep = Annotated[Seller,Depends(get_current_seller)]

ProductDep = Annotated[ProductService,Depends(get_product_service)]


def get_seller_service(session: SessionDep):
    return SellerService(session)  

SellerServiceDep = Annotated[SellerService,Depends(get_seller_service)]