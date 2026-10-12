# Lecture 2.3 - API documentation (Swagger /docs, ReDoc /redoc, Scalar /scalar)
# Extra install:  pip install scalar-fastapi
from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

app = FastAPI(title="Product Store API")


@app.get("/product")
def get_product():
    return {"name": "Wireless Mouse", "price": 18.99, "stock": 42}


# Scalar API documentation (hidden from the schema itself)
@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )
