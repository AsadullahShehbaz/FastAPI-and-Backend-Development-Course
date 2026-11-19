from contextlib import asynccontextmanager
from time import perf_counter
from fastapi import FastAPI,Request, Response
from fastapi.responses import HTMLResponse
from scalar_fastapi import get_scalar_api_reference
from app.api import router
from app.core.exception import add_exception_handler
from app.database.session import create_db_tables
from app.worker.tasks import write_access_log
from fastapi.middleware.cors import CORSMiddleware

tags_metadata = [
    {
        "name": "Product",
        "description": "Create and manage products for delivery.",
    },
    {
        "name": "Seller",
        "description": "Operations available to sellers.",
    },
    {
        "name": "Delivery Partner",
        "description": "Accept deliveries and update their status.",
    },
]

frontend_origins = [
    "*"
]
description ="""AsadullahAIShip helps sellers and delivery partners manage deliveries.
    
### For sellers
- Submit products for delivery.
- Share tracking links with customers.

### For delivery partners
- Accept available deliveries.
- Track and update delivery status.
- Send status notifications.
    """
@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_tables()
    yield
    # Cleanup code can go here if needed


app = FastAPI(lifespan=lifespan,
              title="AsadullahAIShip API",
              summary="Delivery management for sellers and delivery partners",
        description=description,
            version="1.0.0",
            terms_of_service="http://asadullahaiship.com/terms_of_services",
            contact={
                "name": "AsadullahAIShip Support",
                "url": "https://asadullahaiship.example.com/support",
                "email": "support@asadullahaiship.example.com",
            },
            docs_url="/docs",
            openapi_tags=tags_metadata)
app.include_router(router.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods=["GET","POST","PATCH"],
    allow_headers=["Authorization","Content-Type"],
    allow_credentials=False 

)

@app.middleware("http")
async def custom_middleware(request: Request,call_next):

    start = perf_counter()
    response = await call_next(request)

    end = perf_counter()

    total_time = end - start

    response.headers["X-Process-Time"] = f"{total_time:.4f}"
    write_access_log(f"Total Response time : {total_time} {request.method} {request.url.path} {response.status_code}")

    return response 

add_exception_handler(app)

@app.get("/scalar", include_in_schema=False)
async def scalar_docs() -> HTMLResponse:
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )

@app.get("/")
def home():
    return "Welcome to Asadullah AI FastAPI Course Part 3"