from fastapi import BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import Seller
from app.api.schema.seller import SellerCreate
from app.services.user import UserService

class SellerService(UserService):
    def __init__(self,session: AsyncSession,tasks: BackgroundTasks):
        super().__init__(Seller,session,tasks)

    async def add(self,credentials: SellerCreate)-> Seller:
        return await self._add_user(credentials.model_dump(),router_prefix="seller")

    async def login(self,email , password)->str:
      return await self._generate_token(email,password)
        
        
   