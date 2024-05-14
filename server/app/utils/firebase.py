import os
import uuid
import firebase_admin
from firebase_admin import credentials, db, auth
from dotenv import load_dotenv


load_dotenv()

FIREBASE_URL = os.environ.get("FIREBASE_URL")
print(FIREBASE_URL)
cred = credentials.Certificate('service_account.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': FIREBASE_URL  
})

class User:
    def __init__(self, **kwargs):
        self.email = kwargs["email"]
        self.name = kwargs["name"]


class Firebase:
    def set(self, ref, data={}):
        ref = db.reference(ref)
        ref.set(data)
        print('Data has been successfully set in the database.')

    def delete_data(self, ref):
        ref = db.reference(ref)
        ref.delete()

    def get_data(self, ref):
        ref = db.reference(ref)
        return ref.get()
    
    def user_exists(self, ref):
        doc_ref = db.collections(ref)
        doc = doc_ref.get()
        if doc.exists:
            return True
        return False
    
FIRE = Firebase()
import logging
if __name__=="__main__":
    logging.basicConfig(level=logging.DEBUG)

    print("hello")
    ref = db.reference("users/john")
    print(ref.get())
    # print(FIRE.get_data("users/john"))