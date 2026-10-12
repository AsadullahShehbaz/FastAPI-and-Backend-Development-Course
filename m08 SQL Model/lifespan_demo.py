# Lecture 8.3 - Lifespan handler: code on server startup / shutdown
# Run:  fastapi dev m08/lifespan_demo.py     (extra install: pip install rich)
from contextlib import asynccontextmanager

from fastapi import FastAPI
from rich import print
from rich.panel import Panel


@asynccontextmanager
async def lifespan_handler(app: FastAPI):
    print(Panel("Server started...", border_style="green"))     # startup
    yield                                                        # server runs here
    print(Panel("...server stopped", border_style="red"))       # shutdown


app = FastAPI(lifespan=lifespan_handler)


@app.get("/")
def root():
    return {"detail": "server is running"}
