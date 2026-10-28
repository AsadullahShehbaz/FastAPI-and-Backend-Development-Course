from contextlib import asynccontextmanager
from fastapi import BackgroundTasks, FastAPI
from app.api import router
from app.database.session import create_db_tables
from app.services.notification import NotificationService


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_tables()
    yield
    # Cleanup code can go here if needed

app = FastAPI(lifespan=lifespan)
app.include_router(router.router)



