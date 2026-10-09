from typing import Annotated
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession, async_session
from app.database.session import get_session
from app.services.product import ProductService


SessionDep = Annotated[AsyncSession,Depends(get_session)]

def get_product_service(session: SessionDep):
    return ProductService(session)  

ServiceDep = Annotated[ProductService,Depends(get_product_service)]