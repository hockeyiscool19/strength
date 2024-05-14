import uuid
import json
import requests
from fastapi import APIRouter, Request, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from google_auth_oauthlib.flow  import InstalledAppFlow
from server.app.utils.auth import Login, SignUp, ResetPassword
from server.app.utils.firebase import FIRE

router = APIRouter()

with open("oauth.json", "r") as s:
    oauth = json.load(s)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl=oauth["web"]["auth_uri"])


@router.post("/sign_up")
async def sign_up(sign_up: SignUp):
    id=uuid.uuid1()
    return ""
    # print(sign_up, sign_up.email)
    # user = auth.create_user(
    #     email=sign_up.email,
    #     phone_number=sign_up.phone,
    #     password=sign_up.password,
    #     display_name=sign_up.full_name,
    #     disabled=False,
    #     email_verified=False
    # )
    # return sign_up


@router.post("/login")
async def login(sign_in: Login):
    input_username, input_password = sign_in.username, sign_in.password
    # user = FIRE.get_data(f"users/{input_username}")
    # if user == None:
    #     raise HTTPException(status_code=400, detail="User Not Found")
    # password = user["settings"]["password"]
    # if password != input_password:
    #     raise HTTPException(status_code=400, detail="Incorrect Password")
    return {"token": input_username}


@router.post("/reset_password")
async def reset_password(reset_password: ResetPassword):
    return ""
    # reset = auth.generate_password_reset_link(reset_password.email)
    # return {"message": reset}


@router.get("/state")
async def change_state(request: Request):
    return request.app.state.n_client.username
