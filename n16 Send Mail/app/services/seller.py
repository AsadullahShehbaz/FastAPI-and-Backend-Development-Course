from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import Seller
from app.api.schema.seller import SellerCreate
from app.services.user import UserService

class SellerService(UserService):
    def __init__(self,session: AsyncSession):
        super().__init__(Seller,session)

    async def add(self,credentials: SellerCreate)-> Seller:
        return await self._add_user(credentials.model_dump())

    async def login(self,email , password)->str:
      return await self._generate_token(email,password)
        
        
   