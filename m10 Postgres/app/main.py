# Module 10 - Async FastAPI + PostgreSQL + router + service layer
# Run (from the m10 folder):  fastapi dev app/main.py
from contextlib import asynccontextmanager

from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

from app.api.router import router
from app.database.session import create_db_tables, seed_products


@asynccontextmanager
async def lifespan_handler(app: FastAPI):
    await create_db_tables()       # now a coroutine -> await it
    await seed_products()
    yield


app = FastAPI(lifespan=lifespan_handler)

app.include_router(router)         # plug the router into the app


### Scalar API documentation
@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )
