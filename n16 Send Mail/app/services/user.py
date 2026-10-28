from fastapi import HTTPException

from app.database.models import User
from app.services.base import BaseService

from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.utils import generate_access_token
# Initialize object 
pwd_context = CryptContext(schemes="bcrypt")

class UserService(BaseService):
    def __init__(self,model: type[User],session: AsyncSession):
        super().__init__(model,session)

    # Get user by email 
    async def _get_by_email(self,email:str )-> User | None:  
        return await self.session.scalar(select(self.model).where(self.model.email == email))
    
    # Ad user 
    async def _add_user(self,data: dict)-> User:
        password = data.pop("password")

        user = self.model(
            **data,
            password_hash=pwd_context.hash(password)
        )
        return await self._add(user)

    
    # Generate Token 
    async def _generate_token(self,email : str , password: str)->str:
            # Validating credentials in the client request 
            user = await self._get_by_email(email)
            if user is None or not pwd_context.verify(password,user.password_hash):
                raise HTTPException(
                    status_code=401,
                    detail="Email or password is not correct"
                )
            # Generate Access Token 
            return generate_access_token( 
                {
                    "user":{
                        "id": str(user.id)
                    }
                }
            )
    