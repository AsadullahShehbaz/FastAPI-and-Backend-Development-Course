from fastapi import HTTPException
from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext

from app.database.models import Seller
from app.api.schema.seller import SellerCreate
from app.utils import generate_access_token


# Initialize object 
pwd_context = CryptContext(schemes="bcrypt")

class SellerService:
    def __init__(self,session: AsyncSession):
        self.session = session 

    async def add(self,credentials: SellerCreate)-> Seller:
        seller = Seller(
            **credentials.model_dump(exclude={"password"}),
            password_hash=pwd_context.hash(credentials.password)
        )
        self.session.add(seller)
        await self.session.commit()
        await self.session.refresh(seller)
        return seller

    async def login(self,email , password)->str:
        # Validating credentials in the client request 
        result = await self.session.execute(select(Seller).where(Seller.email == email))
        seller = result.scalar()

        if seller is None or not pwd_context.verify(password,seller.password_hash):
            raise HTTPException(
                status_code=401,
                detail="Email or password is not correct"
            )
        # Generate Access Token 
        token = generate_access_token(
            {
                "user":{
                    "id": seller.id
                }
            }
        )
        return token 
        
        
   