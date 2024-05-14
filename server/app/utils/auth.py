from base64 import b64encode, b64decode
from pydantic import BaseModel

class SignUp(BaseModel):
    email: str
    phone: str
    password: str
    full_name: str

class Login(BaseModel):
    username: str
    password: str

class ResetPassword(BaseModel):
    email: str

class User:
    def __init__(self, **kwargs):
        self.email = kwargs["email"]
        self.name = kwargs["name"]

def encrypt(input_string):
    return b64encode(bytes(input_string, "utf-8"))

def decrypt(input_string):
    return b64decode(input_string)

if __name__=="__main__":
    s = "str"
    print(decrypt(encrypt("hello world")))