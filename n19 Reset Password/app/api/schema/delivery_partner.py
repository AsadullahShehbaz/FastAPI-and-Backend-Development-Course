from pydantic import BaseModel, EmailStr


class BaseDeliveryPartner(BaseModel):
    name: str
    email: EmailStr
    serviceable_zip_codes: list[int]     # extra field: areas they deliver to
    max_handling_capacity: int           # extra field: how many parcels at once

class DeliveryPartnerRead(BaseDeliveryPartner):
    pass 


class DeliveryPartnerCreate(BaseDeliveryPartner):
    password: str                      

class DeliveryPartnerUpdate(BaseModel):
    serviceable_zip_codes: list[int] | None = None
    max_handling_capacity: int | None = None
