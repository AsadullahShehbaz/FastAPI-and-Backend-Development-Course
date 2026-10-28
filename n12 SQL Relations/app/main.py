from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api import router
from app.database.session import create_db_tables
from scalar_fastapi import get_scalar_api_reference

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_tables()
    yield
    # Cleanup code can go here if needed

app = FastAPI(lifespan=lifespan)
app.include_router(router.router)

### Scalar API Documentation
@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )
