from typing import Annotated

from fastapi import Form, HTTPException, Request, status
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import Field

from app.api.schema.product import ProductCreate, ProductRead, ProductReview, ProductUpdate
from app.api.dependencies import DeliveryPartnerDep, ProductDep, SellerDep, SessionDep
from app.api.schema.product import ProductRead
from app.config import app_settings
from uuid import UUID

from app.core.exception import EntityNotFound
from app.database.models import TagName
from app.utils import TEMPLATE_DIR


router = APIRouter(prefix="/product/v1", tags=["Product"])

templates = Jinja2Templates(TEMPLATE_DIR)

@router.post("/tag",response_model=ProductRead)
async def add_tag_to_product(id: UUID, tag_name: TagName, service: ProductDep):
    return await service.add_tag(id, tag_name)

@router.delete("/tag",response_model=ProductRead)
async def remove_tag_from_product(id: UUID, tag_name: TagName, service: ProductDep ):
    return await service.remove_tag(id, tag_name)

@router.get("/tagged",response_model=list[ProductRead])
async def get_products_by_tag(tag_name: TagName, session: SessionDep ):
    tag = await tag_name.tag(session)
    return tag.products 
@router.post('/review')
async def submit_review(token: str,
                        service: ProductDep,
                        rating: Annotated[int,Form(ge=1,le=5)],
                        comment: Annotated[str | None ,Form()] = None,
                        ):
    
    await service.rate(token,rating,comment)
    return {"detail":"Review Submitted"}

@router.get("/review")
async def get_review_form(request: Request,token: str):
    review_url = f"http://{app_settings.APP_DOMAIN}{router.prefix}/review?token={token}"

    return templates.TemplateResponse(
        request=request,
        name="review.html",
        context = {"review_url": review_url}
    )

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

    return await service.get(id)



@router.post("/",
            summary="Create a product",
            description="Submit a product for delivery. **Sellers** can track it after creation.",
            response_model=ProductRead,
            status_code=status.HTTP_201_CREATED,
            responses={
            406: {
                "description": "No delivery partner is available.",
                "content": {
                    "application/json": {
                        "example": {
                            "detail": "No delivery partner is available."
                        }
                    }
                },
            }
    },)
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



