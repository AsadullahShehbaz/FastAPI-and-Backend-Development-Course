from fastapi import HTTPException, Request, status
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.api.schema.product import ProductCreate, ProductRead, ProductUpdate
from app.api.dependencies import DeliveryPartnerDep, ProductDep, SellerDep
from app.api.schema.product import ProductRead
from uuid import UUID

from app.utils import TEMPLATE_DIR


router = APIRouter(prefix="/product/v1", tags=["Product"])

templates = Jinja2Templates(TEMPLATE_DIR)

@router.get("/track",include_in_schema=False)
async def get_tracking(request: Request,id: UUID, service: ProductDep):
    product = await service.get(id)

    context = product.model_dump()
    context["status"] =  product.status
    context["seller"] =  product.seller.name
    context["partner"] =  product.delivery_partner.name
    context["timeline"] =  product.timeline[::-1]


    return templates.TemplateResponse(
        request = request, 
        name = "track.html",
        context = context
    )

@router.get("/{id}",response_model=ProductRead)
async def get_product(id: UUID,service: ProductDep ) -> dict:

    product = await service.get(id)
    # Check whether the requested product exists
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product with the given ID was not found!",
        )

    return product



@router.post("/")
async def create_product(data: ProductCreate, seller : SellerDep, service: ProductDep ) -> ProductRead:

    return await service.add(data,seller)


@router.patch("/")
async def patch_product(id : UUID, 
                  body: ProductUpdate,
                  partner : DeliveryPartnerDep,
                  service: ProductDep 
                  )-> ProductRead:

    if not body.model_dump(exclude_none=True):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "No data provided to update")
    return await service.update(id, body,partner)

@router.get("/",response_model=ProductRead)
async def cancel_product(id: UUID, seller : SellerDep,service: ProductDep ):
    return await service.cancel(id,seller)


