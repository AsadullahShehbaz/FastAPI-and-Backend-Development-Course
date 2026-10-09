from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.routers import product
from app.database.session import create_db_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_tables()
    yield
    # Cleanup code can go here if needed

app = FastAPI(lifespan=lifespan)
app.include_router(product.router)


