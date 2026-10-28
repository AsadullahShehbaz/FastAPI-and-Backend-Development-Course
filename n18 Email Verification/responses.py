# Response Classes and custom responses

from datetime import datetime
import time
from typing import Any

from fastapi import FastAPI, Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import FileResponse, JSONResponse,HTMLResponse, PlainTextResponse, RedirectResponse, StreamingResponse
from sqlalchemy import JSON
import uvicorn

app = FastAPI()

PATH = "asadullahai.txt"


class UpperResponse(Response):
    def __init__(self, content = None, status_code = 200, headers = None, media_type = None, background = None):
        super().__init__(content, status_code, headers, media_type, background)

    def render(self, content):
        return super().render(content.upper())



@app.get("/",response_class=UpperResponse)
def home():
    return "asadullah ai"

if __name__ == "__main__":
    uvicorn.run(app="main:app",host="127.0.0.1",port=8000,reload=True)

# uvicorn main:app --reload