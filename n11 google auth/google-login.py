import json
import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from authlib.integrations.starlette_client import OAuth

load_dotenv()

app = FastAPI()

app.add_middleware(
    SessionMiddleware,
    secret_key=os.environ["SESSION_SECRET"],
    same_site="lax",
    https_only=False,
)

oauth = OAuth()
oauth.register(
    name="google",
    client_id=os.environ["GOOGLE_CLIENT_ID"],
    client_secret=os.environ["GOOGLE_CLIENT_SECRET"],
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)


@app.get("/login/google")
async def login_google(request: Request):
    redirect_uri = request.url_for("auth_google")
    return await oauth.google.authorize_redirect(request, redirect_uri)


@app.get("/auth/google")
async def auth_google(request: Request):
    token = await oauth.google.authorize_access_token(request)
    user = token["userinfo"]

    request.session["user"] = {
        "google_id": user["sub"],
        "email": user["email"],
        "name": user.get("name"),
        "picture": user.get("picture"),
    }

    return RedirectResponse(url="/", status_code=303)


@app.get("/me")
async def get_current_user(request: Request):
    user = request.session.get("user")

    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")

    return {
        "message": "User authenticated successfully",
        "user": user,
    }


@app.get("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/")

from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def homepage(request: Request):

    user = request.session.get("user")

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"user": user}
    )
