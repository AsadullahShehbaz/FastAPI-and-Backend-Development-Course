from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import DeliveryPartner, Location, Seller
from app.services.user import pwd_context

SELLER = {
    "name": "Asadullah",
    "email": "seller@gmail.com",
    "password": "asadullahai",
    "zip_code": 20,
}

DELIVERY_PARTNER = {
    "name": "Anas",
    "email": "partner@gmail.com",
    "password": "fastapicourse",
    "zip_code": 22,
    "max_handling_capacity": 5,                      # more headroom
    "serviceable_zip_codes": [22, 12, 20, 16, 10],   # must include PRODUCT["destination"]
}

# Matches ProductCreate
PRODUCT = {
    "name": "Marse Pro",
    "price": 122.0,
    "stock": 22,
    "destination": 22,                               # must be in serviceable_zip_codes
    "client_contact_email": "client@gmail.com",
    "client_contact_phone": "+92322122022",         # optional field
}


async def create_test_data(session: AsyncSession) -> None:
    seller_data = {k: v for k, v in SELLER.items() if k != "password"}
    partner_data = {
        k: v
        for k, v in DELIVERY_PARTNER.items()
        if k not in ("password", "serviceable_zip_codes")
    }

    session.add(
        Seller(
            **seller_data,
            email_verified=True,
            password_hash=pwd_context.hash(SELLER["password"]),
        )
    )
    session.add(
        DeliveryPartner(
            **partner_data,
            email_verified=True,
            password_hash=pwd_context.hash(DELIVERY_PARTNER["password"]),
            serviceable_locations=[
                Location(zip_code=z)
                for z in DELIVERY_PARTNER["serviceable_zip_codes"]
            ],
        )
    )
    await session.commit()
