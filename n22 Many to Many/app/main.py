from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api import router
from app.database.session import create_db_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_tables()
    yield
    # Cleanup code can go here if needed

app = FastAPI(lifespan=lifespan)
app.include_router(router.router)

from datetime import datetime
from app.worker.tasks import background_task

@app.get("/test")
def test():
    now = datetime.now()
    background_task.delay(
        name=now.second,
        data={"minute": now.minute, "second": now.second},
    )
    return {"detail": "task queued"}



