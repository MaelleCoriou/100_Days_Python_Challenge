import os
import requests

# Get user name, last name and email address to save in google sheet

TOKEN = os.environ.get("SHEETY_TOKEN")
ENDPOINT = os.environ.get("URL_PRICES_ENDPOINT")

print("Welcome to Maëlle's Flight Club\nWe find the best flight deals and email you")

name = str(input("What is your name? \n")).title()

last_name = str(input("What is your last_name? \n")).title()

email = str(input("What is your email? \n"))

email_check = str(input("Please confirm your email again: \n"))


while email != email_check:
    email_check = str(input("Emails entered don't match, please enter your email again: \n"))

header = {
            "Authorization": f"bearer {TOKEN}"
        }

new_data = {
            "user": {
                "firstName": name,
                "lastName": last_name,
                "email": email
            }
        }

response = requests.post(
            url=f"{ENDPOINT}users",
            json=new_data,
            headers=header
        )
        
response.raise_for_status()

