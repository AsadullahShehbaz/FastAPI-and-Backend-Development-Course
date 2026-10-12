from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_session
from app.services.product import ProductService

# 1) async database session dependency
SessionDep = Annotated[AsyncSession, Depends(get_session)]


# 2) service dependency - it DEPENDS on the session (dependency chaining)
def get_product_service(session: SessionDep):
    return ProductService(session)       # plain def: nothing to await here


ServiceDep = Annotated[ProductService, Depends(get_product_service)]
