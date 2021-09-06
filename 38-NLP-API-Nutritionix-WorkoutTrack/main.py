import requests
import os
from datetime import datetime

# Get Nutritionix + Sheety access codes
NUTRITION_ID = os.environ.get("NUTRITIONIX_ID")
NUTRITION_KEY = os.environ.get("NUTRITIONIX_KEY")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
ENDPOINT = os.environ.get("URL_SHEET_ENDPOINT")

# Today's date set up
TODAY = datetime.now().strftime("%d/%m/%Y")
TIME = datetime.now().time().strftime("%X")

# ---------------------- NUTRITIONIX POST SET UP -----------------------#

# Authorization headers set up
header= {
    "x-app-id": NUTRITION_ID,
    "x-app-key": NUTRITION_KEY,
    "Content-Type": "application/json"
}

# Request fields set up
request_body = {
    "query": input("What's your today workout? "),
    "gender": "female",
    "weight_kg": 47,
    "height_cm": 156,
    "age": 41
}

# Get info regarding request body and input
exercise_url = requests.post("https://trackapi.nutritionix.com/v2/natural/exercise",
                             headers=header,
                             json=request_body)
exercise_url.raise_for_status()

data = exercise_url.json()["exercises"][0]
# print(data)

# ---------------------- SHEETY POST SET UP -----------------------#

header = {
    "Authorization": f"bearer {SHEETY_TOKEN}"
}

# New entries based on Nutritionix input and response
new_row = {
    "workout": {
        "date": TODAY,
        "time": TIME,
        "exercise": data["name"].title(),
        "duration": data["duration_min"],
        "calories": data["nf_calories"]
    }
}

# Read current info in spreadsheet
sheety_url = requests.get(ENDPOINT,
                          headers=header)
print(sheety_url.text)


# Add new line POST request to spreadsheet google drive via sheety
new_line = requests.post(ENDPOINT,
                         json=new_row,
                         headers=header)
print(new_line.text)