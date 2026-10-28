from typing import Annotated

from fastapi import APIRouter, Depends, Form, Request
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates
from pydantic import EmailStr
from app.api.dependencies import SellerServiceDep, get_seller_access_token
from app.database.redis import add_jti_to_blacklist
from app.utils import TEMPLATE_DIR
from ..schema.seller import SellerCreate, SellerRead
from app.config import app_settings

router = APIRouter(prefix="/seller",tags=['Seller'])

@router.post("/signup")
async def register_seller(seller: SellerCreate,service: SellerServiceDep)-> SellerRead:
    return await service.add(seller)

@router.post("/login")
async def login(
    service: SellerServiceDep,
    request_form: OAuth2PasswordRequestForm = Depends(),
    ) -> dict:
    token = await service.login(request_form.username,request_form.password)

    return {
            "access_token":token,
            "type":"jwt"
    }

@router.get("/logout")
async def logout_seller(token_data : Annotated[dict,Depends(get_seller_access_token)]):

    await add_jti_to_blacklist(token_data["jti"])
    return {"detail": "Successfully logged out"}

@router.get("/verify")
async def verify_seller_email(token: str,service: SellerServiceDep):
    await service.verify_email(token)
    return {"detail":"Account Verified"}


# Email password reset link
@router.get("/forgot_password")
async def forgot_password(email: EmailStr,service: SellerServiceDep):
    await service.send_password_reset_link(email,router.prefix)
    return {"detail":"Check email for password reset link"}


# Show new password form
@router.get("/reset_password_form")
async def reset_password_form(request: Request,token: str,service: SellerServiceDep):
    templates = Jinja2Templates(TEMPLATE_DIR)

    return templates.TemplateResponse(
        request=request,
        name="password/reset.html",
        context={
            "reset_url": f"http://{app_settings.APP_DOMAIN}{router.prefix}/reset_password?token={token}"
        }
    )

# Save new password
@router.post("/reset_password")
async def reset_password(request: Request, token: str, password: Annotated[str,Form()] ,service: SellerServiceDep):
    is_success = await service.reset_password(token,password)

    templates = Jinja2Templates(TEMPLATE_DIR)
    return templates.TemplateResponse(
        request= request,
        name="password/reset_success.html" if is_success else "password/reset_failed"
    ) 