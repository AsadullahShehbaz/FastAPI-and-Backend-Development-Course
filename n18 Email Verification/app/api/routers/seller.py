from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.api.dependencies import SellerServiceDep, get_seller_access_token
from app.database.redis import add_jti_to_blacklist
from ..schema.seller import SellerCreate, SellerRead

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