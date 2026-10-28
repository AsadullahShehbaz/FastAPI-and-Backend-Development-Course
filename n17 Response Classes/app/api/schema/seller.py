from pydantic import BaseModel, EmailStr

class BaseSeller(BaseModel):
    name: str
    email : EmailStr
    address: str | None = None
    zip_code: int | None = None


class SellerCreate(BaseSeller):
    password : str 

class SellerRead(BaseSeller):
    pass 