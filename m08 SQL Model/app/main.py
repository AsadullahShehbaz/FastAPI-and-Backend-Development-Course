# Module 8 - FastAPI + SQLModel + dependency injection
# Run (from the m08 folder):  fastapi dev app/main.py
from contextlib import asynccontextmanager
from datetime import datetime, timedelta, timezone

from fastapi import FastAPI, HTTPException, status

from app.database.models import Product, ProductStatus
from app.database.session import SessionDep, create_db_tables, seed_products

from .schemas import ProductCreate, ProductRead, ProductUpdate


@asynccontextmanager
async def lifespan_handler(app: FastAPI):
    create_db_tables()        # startup: create tables if missing
    seed_products()
    yield                     # (shutdown code would go after yield)


app = FastAPI(lifespan=lifespan_handler)


def not_found() -> HTTPException:
    return HTTPException(status.HTTP_404_NOT_FOUND, "Given id doesn't exist!")


@app.get("/product", response_model=ProductRead)
def get_product(id: int, session: SessionDep):
    product = session.get(Product, id)       # table model + primary key
    if product is None:
        raise not_found()
    return product


@app.post("/product")
def create_product(product: ProductCreate, session: SessionDep) -> dict[str, int]:
    new_product = Product(
        **product.model_dump(),
        status=ProductStatus.active,
        warranty_until=datetime.now(timezone.utc) + timedelta(days=365),
    )
    session.add(new_product)         # stage
    session.commit()                 # save
    session.refresh(new_product)     # reload -> the database-made id is now set

    return {"id": new_product.id}


@app.patch("/product", response_model=ProductRead)
def update_product(id: int, product_update: ProductUpdate, session: SessionDep):
    update = product_update.model_dump(exclude_none=True)
    if not update:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "No data provided to update")

    product = session.get(Product, id)
    if product is None:
        raise not_found()

    product.sqlmodel_update(update)   # copy only the given fields
    session.add(product)
    session.commit()
    session.refresh(product)
    return product


@app.delete("/product")
def delete_product(id: int, session: SessionDep) -> dict[str, str]:
    product = session.get(Product, id)
    if product is None:
        raise not_found()

    session.delete(product)
    session.commit()
    return {"detail": f"Product with id #{id} is deleted!"}
