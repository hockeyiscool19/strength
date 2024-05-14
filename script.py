# import requests
# import json
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys

# # Constants
# auth_uri = "https://accounts.google.com/o/oauth2/auth"
# token_uri = "https://oauth2.googleapis.com/token"
# redirect_uri = "http://localhost:8081/redirect"
# scope = "https://www.googleapis.com/auth/drive.file"
# client_id, client_secret = None, None

# def load_credentials():
#     """
#     Load client ID and client secret from a JSON file.
#     """
#     with open('oauth.json', 'r') as file:
#         data = json.load(file)
#     global client_id, client_secret
#     client_id = data['web']['client_id']
#     client_secret = data['web']['client_secret']

# def get_authorization_code():
#     """
#     Use Selenium to open a browser and automatically log in and authorize the app.
#     """
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option("excludeSwitches", ["enable-logging"])
#     driver = webdriver.Chrome(options=options)
    
#     params = {
#         "client_id": client_id,
#         "redirect_uri": redirect_uri,
#         "response_type": "code",
#         "scope": scope,
#         "access_type": "offline",
#         "prompt": "consent"
#     }
#     url = requests.Request('GET', auth_uri, params=params).prepare().url
#     driver.get(url)
    
#     # Automatically handle login and authorization here
#     # You will need to fill in the username and password, and handle buttons
#     # Example:
#     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "identifierId"))).send_keys('your-email@gmail.com')
#     driver.find_element(By.ID, "identifierId").send_keys(Keys.RETURN)
#     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "password"))).send_keys('your-password')
#     driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)

#     # Wait for the redirect and parse the URL for the authorization code
#     WebDriverWait(driver, 20).until(EC.url_contains("code="))
#     redirect_url = driver.current_url
#     driver.quit()
#     code = redirect_url.split('code=')[1].split('&')[0]
#     return code

# def exchange_code_for_tokens(code):
#     """
#     Exchange the authorization code for an access token and a refresh token
#     """
#     data = {
#         "code": code,
#         "client_id": client_id,
#         "client_secret": client_secret,
#         "redirect_uri": redirect_uri,
#         "grant_type": "authorization_code"
#     }
#     response = requests.post(token_uri, data=data)
#     return response.json()

# def main():
#     load_credentials()
#     code = get_authorization_code()
#     tokens = exchange_code_for_tokens(code)
#     print("Access Token:", tokens.get("access_token"))
#     print("Refresh Token:", tokens.get("refresh_token"))

# if __name__ == "__main__":
#     main()


from firebase_admin import credentials, db, initialize_app
import os
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)
load_dotenv()

FIREBASE_URL = os.environ.get("FIREBASE_URL")
cred = credentials.Certificate("serviceAccountKey.json")
initialize_app(cred, {
    'databaseURL': FIREBASE_URL  
})

if __name__ == "__main__":
    ref = db.reference("users")
    print(ref.get())