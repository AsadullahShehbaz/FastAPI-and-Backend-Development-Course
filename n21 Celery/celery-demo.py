from datetime import datetime

from fastapi import FastAPI
import uvicorn

from app.worker.tasks import background_tasks


app = FastAPI()

@app.get("/")
def home():
    now = datetime.now()
    background_tasks.delay(
        f"Background Tasks {now.second}",
        data={
            "min": now.minute,
            "sec": now.second
        }
    )
    return {"Result":"Task executed with Celery"}

if __name__ == "__main__":
    uvicorn.run(app="main:app",host="127.0.0.1",port=8000,reload=True)