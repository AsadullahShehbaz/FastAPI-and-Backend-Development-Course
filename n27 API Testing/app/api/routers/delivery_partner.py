from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.api.dependencies import DeliveryPartnerServiceDep,DeliveryPartnerDep
from app.api.schema.delivery_partner import DeliveryPartnerCreate, DeliveryPartnerRead, DeliveryPartnerUpdate


router = APIRouter(prefix="/partner", tags=["Delivery Partner"])

@router.post("/")
async def update_delivery_partner(
    partner_update: DeliveryPartnerUpdate,
    partner : DeliveryPartnerDep,          # only a logged-in partner can reach this
    service: DeliveryPartnerServiceDep,   # type annotation added later
):
   return await service.update(partner.id,partner_update)


@router.post("/signup", response_model=DeliveryPartnerRead)
async def register_delivery_partner(
    partner: DeliveryPartnerCreate,
    service: DeliveryPartnerServiceDep,   
):
    return await service.add(partner)

@router.post("/login")
async def login_delivery_partner(
    request_form: Annotated[OAuth2PasswordRequestForm, Depends()],
    service: DeliveryPartnerServiceDep,
):
    token = await service.login(request_form.username, request_form.password)
    return {"access_token": token, "type": "jwt"}

@router.get("/verify")
async def verify_partner_email(token: str,service: DeliveryPartnerServiceDep):
    await service.verify_email(token)
    return {"detail":"Account Verified"}