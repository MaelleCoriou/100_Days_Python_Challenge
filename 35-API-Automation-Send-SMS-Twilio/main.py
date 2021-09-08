import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


#--------------------- WEATHER SMS ALERT --------------------------#


## Download the helper library from https://www.twilio.com/docs/python/install
## Proxy client for PythonAnywhere automation
# proxy_client = TwilioHttpClient()
# proxy_client.session.proxies = {"https": os.environ["https_proxy"]}

# Get os variables for Twilio access, website : https://console.twilio.com
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

# Get contact to send SMS to
contact = os.environ.get("PHONE")

# For PythonAnywhere, automation os variables won't show up
# Key=value variable need to be set up in the schedule task before program path:
# account_sid="ACa8cxxxxxxxxxxxx";auth_token="3a1xxxxxxxxxxxxxxx";key=xxxxx;contact=xxxxxx;/home/MaelleCo/TODAY_WEATHER/main.py

client = Client(account_sid, auth_token) #http_client=proxy_client

# Get Weather API key API website https://openweathermap.org/api
key = os.environ.get("WEATHER_API_KEY")

# 7 days forecast:
parameters = {
    "lat": "47.218371",
    "lon": "-1.553621",
    "exclude": "current,minutely,daily",
    "appid": key
}

# Connect with open weather map API key, documentation: https://openweathermap.org/api/one-call-api
request = requests.get(url="https://api.openweathermap.org/data/2.5/onecall?",
                       params=parameters)
request.raise_for_status()

data = request.json()

# # In 12 hour weather request
# hour_weather = data["hourly"][12]["weather"][0]["id"]
# if hour_weather < 700:
#     print("Bring an umbrella!")
# else:
#     print("Weather is good today!")

# Get the 11 upcoming hours' weather
weather_slice = data["hourly"][0:12]

will_rain = False

for hours in weather_slice:
    # To get the weather info dic
    condition_code = hours["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
        print(condition_code)


def message():
    if will_rain:
        return "Bring an ☂"
    else:
        return "Weather is good today!"


# SMS message set up
message = client.messages \
                .create(
                     body=f"{message()}",
                     from_="+19473338388",
                     to=contact
                 )

print(message.status)
