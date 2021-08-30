##################        API        ##################


"""API endpoints are the location of data, usually the URL of the website
    Ex: api.coinbase.com,
    API request to get the response info, output in json format """

import requests
from datetime import datetime
import SMTP_Set_up
from pw import CONTACT
import time

# My position
nantes_latitude = 47.218371
nantes_longitude = -1.553621


def iss_visible():
    """Returns True if current ISS position is close"""

    # ISS location API
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    # response 1XX = on hold, 2XX = successful, 3XX = permission denied, 5XX = Server error
    # print(response)
    # print(response.status_code)

    # To get the error type if response isn't 200
    response.raise_for_status()

    # To get response data, full data
    data = response.json()

    # To get specific info with full data request
    # iss_position = response.json()

    # To get a specific info with request.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    if nantes_latitude - 5 <= iss_latitude <= nantes_latitude + 5 \
            and nantes_longitude - 5 <= iss_longitude <= nantes_longitude + 5:
        return True


def is_dark():
    """Returns True if it's night time"""

    response = requests.get(
        f"https://api.sunrise-sunset.org/json?lat={nantes_latitude}&lng={nantes_longitude}&formatted=0")

    # Other parameters set up
    # parameters = {
    #     "lat": nantes_latitude,
    #     "lng": nantes_longitude
    # }
    # response = requests.get(f"https://api.sunrise-sunset.org/json", params=parameters)

    data = response.json()
    # Get the hour of sunset and sunrise of the current day
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])

    # Now hour
    now = datetime.now().time().hour
    if now >= sunset or now <= sunrise:
        return True


while True:
    # Refresh every 60 seconds.
    time.sleep(60)
    if iss_visible() and is_dark():
        SMTP_Set_up.send_email(message=f"Subject: ISS is close!\n\nLook up to the sky, ISS is passing by!",
                               contact=CONTACT)
