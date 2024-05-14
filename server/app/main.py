import os
import uuid
import json
import requests
from fastapi import FastAPI, Request, APIRouter
from contextlib import asynccontextmanager

from server.app.utils.firebase import auth
from server.app.utils.auth import SignUp, ResetPassword
from server.app.utils.state import context
from server.app.routes.auth import router

API_KEY = os.environ.get("FIREBASE_WEB_API_KEY")

@asynccontextmanager
async def lifespan(app: FastAPI):
    ''' Run at startup
        Initialise the Client and add it to app.state
    '''
    app.state = context
    print(app.state, " state")
    yield
    ''' Run on shutdown
        Close the connection
        Clear variables and release the resources
    '''
    app.state.n_client.close()


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/redirect")
async def root():
    return {"message": "You have been redirected"}


app.include_router(router, prefix="/auth")
