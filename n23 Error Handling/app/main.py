from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from app.api import router
from app.core.exception import InValidToken, add_exception_handlers
from app.database.session import create_db_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_tables()
    yield
    # Cleanup code can go here if needed

app = FastAPI(lifespan=lifespan)
app.include_router(router.router)

# @app.exception_handler(InValidToken)
# def invalid_token_handler(request: Request, exception: InValidToken):
#     raise HTTPException(
#         detail={"detail": "Token is invalid or expired"},
#         status_code=400,
#     )
# app.add_exception_handler(InValidToken,invalid_token_handler)

add_exception_handlers(app)

