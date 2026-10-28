from datetime import timedelta
from fastapi import BackgroundTasks, HTTPException

from app.database.models import User
from uuid import UUID
from app.services.base import BaseService

from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.notification import NotificationService
from app.config import app_settings
from app.utils import decode_url_safe_token, generate_access_token, generate_url_safe_token
# Initialize object 
pwd_context = CryptContext(schemes="bcrypt")

class UserService(BaseService):
    def __init__(self,model: type[User],session: AsyncSession,tasks: BackgroundTasks):
        super().__init__(model,session)
        self.notification_service= NotificationService(tasks)

    # Get user by email 
    async def _get_by_email(self,email:str )-> User | None:  
        return await self.session.scalar(select(self.model).where(self.model.email == email))
    
    # Ad user 
    async def _add_user(self,data: dict,router_prefix: str)-> User:
        password = data.pop("password")

        user = self.model(
            **data,
            password_hash=pwd_context.hash(password)
        )
        user =  await self._add(user)

        token = generate_url_safe_token({"id":str(user.id)},salt="emailverification")
        await self.notification_service.send_mail_with_template(
            recipient = [user.email],
            subject="Verify your acccount with AsadullahAIShip",
            context={
                 "username":user.name,
                 "verification_url": f"http://{app_settings.APP_DOMAIN}/{router_prefix}/verify?token={token}"
            },
            template_name="mail-email-verify.html"
        )
        return user

    
    # Generate Token / Login Logic
    async def _generate_token(self,email : str , password: str)->str:
            # Validating credentials in the client request 
            user = await self._get_by_email(email)
            if user is None or not pwd_context.verify(password,user.password_hash):
                raise HTTPException(
                    status_code=401,
                    detail="Email or password is not correct"
                )

            # Block users who have not verified email 
            if not user.email_verified:
                 raise HTTPException(
                    status_code=401,
                    detail="Email not verified"
                )
            # Generate Access Token 
            return generate_access_token( 
                {
                    "user":{
                        "id": str(user.id)
                    }
                }
            )
    async def verify_email(self,token: str):
        token_data = decode_url_safe_token(token,expiry=timedelta(days=1),salt="emailverification")

        if not token_data:
             raise HTTPException(
                  status_code=400,
                  detail="Invalid token"
             )

        user = await self._get(UUID(token_data["id"]))
        user.email_verified=True

        await self._update(user)
    
    async def send_password_reset_link(self,email,router_prefix: str):

         # Get user from db
        user = await self._get_by_email(email)

         # URL Safe token
        token = generate_url_safe_token({"id":str(user.id)},salt="passwordreset")
        await self.notification_service.send_mail_with_template(
            recipient = [user.email],
            subject="AsadullahAIShip Account Password Reset",
            context={
                    "username":user.name,
                    "reset_url": f"http://{app_settings.APP_DOMAIN}{router_prefix}/reset_password_form?token={token}"
            },
            template_name="mail_password_reset.html"
        )

    async def reset_password(self,token: str , password : str)-> bool:
        token_data = decode_url_safe_token(token,expiry=timedelta(days=1),salt="passwordreset")
            
        if not token_data:
            return False
        
        user = await self._get(UUID(token_data["id"]))
        user.password_hash=pwd_context.hash(password)

        await self._update(user)

        return True