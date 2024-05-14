import os
import json
from base64 import b64encode
from dotenv import load_dotenv
from server.app.utils.firebase import FIRE

proportions = open("server/app/fixtures/classification.json", "r")
proportions = json.load(proportions)

user = open("server/app/fixtures/sample_user.json", "r")
user = json.load(user)

if __name__=="__main__":
    print(user.keys())
    # user["John Doe"]["settings"]["password"] = b64encode(bytes(user["John Doe"]["settings"]["password"], "utf-8"))
    # print(user["John Doe"]["settings"]["password"])
    FIRE.set("/fixture", proportions)
    FIRE.set("/users", user)
