# Lecture 2.2 - Your first FastAPI app
# Run:  fastapi dev m02/first_api.py
from fastapi import FastAPI

app = FastAPI(title="Product Store API")


@app.get("/")
def home():
    return {"message": "Product API is running"}


@app.get("/product")
def get_product():
    # dict returned -> FastAPI converts it to JSON
    return {"name": "Wireless Mouse", "price": 18.99, "stock": 42}
