import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import datetime as dt

STOCK = "SCX"
COMPANY_NAME = "Starrett"

# --------------------------- Twilio SET UP --------------------------------#
# # Proxy client for PythonAnywhere automation
# proxy_client = TwilioHttpClient()
# proxy_client.session.proxies = {"https": os.environ["https_proxy"]}

# Get os variables for Twilio
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

# Get contact to send SMS to
contact = os.environ.get("PHONE")

# For PythonAnywhere, automation os variables won't show up
# Key=value variable need to be set up in the schedule task before program path:
# account_sid="ACa8cxxxxxxxxxxxx";auth_token="3a1xxxxxxxxxxxxxxx";key=xxxxx;contact=xxxxxx;/home/MaelleCo/TODAY_WEATHER/main.py

# Create client access Twilio
client = Client(account_sid, auth_token)  # http_client=proxy_client parameter to add for PythonAnywhere

# --------------------------- ALPHA VANTAGE SET UP --------------------------------#
# Get Alpha Vantage API key to get stock info
key_stock = os.environ.get("STOCK_ALPHA_VANTAGE_KEY")

try:
    # 7 days forecast:
    parameters_stock = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": key_stock
    }

    # Connect with API key
    request_stock = requests.get("https://www.alphavantage.co/query?", params=parameters_stock)
    data_stock = request_stock.json()["Time Series (Daily)"]

    # Set today and yesterday variables
    today = dt.datetime.now().date()
    yesterday = str(today - dt.timedelta(days=1))
    two_days_ago = str(today - dt.timedelta(days=2))

    # Get today and yesterday stock values at close time
    yesterday_closing = float(data_stock[yesterday]["4. close"])
    two_days_closing = float(data_stock[two_days_ago]["4. close"])

    # Stock variation
    diff = yesterday_closing - two_days_closing
    variation = round((diff / yesterday_closing) * 100)
    print(variation)

except KeyError:
    print("No stock closing value available.")

else:
    # --------------------------- NEWS SET UP --------------------------------#
    # Get News API key to get latest news info
    key_news = os.environ.get("NEWS_API_KEY")

    # 7 days forecast:
    parameters_news = {
        "qInTitle": COMPANY_NAME,
        "sortBy": "popularity",
        "language": "en",
        "from": yesterday,
        "apiKey": key_news
    }

    # Connect with API key
    request_news = requests.get("https://newsapi.org/v2/everything?", params=parameters_news)
    data_news = request_news.json()["articles"]

    # Get the 3 most popular news
    top_3 = data_news[0:3]

    # Set message, SMS alert conditions and send message
    text = ""
    if variation >= 2 or variation <= -2:
        for article in top_3:
            if variation >= 2:
                text += f"\n{COMPANY_NAME}: 🔺{variation}%\n"
            elif variation <= -2:
                text = f"\n{COMPANY_NAME}: 🔻{variation}%\n"
            text += f"Headline: {article['title']}\n"
            text += f"Brief: {article['description']}\n"
        # Set Twilio SMS if conditions met
        message = client.messages \
            .create(
                    body=f"{text}",
                    from_="+19473338388",
                    to=contact
                    )
        print(message.status)

    print(yesterday_closing)
    print(two_days_closing)
    print(top_3)
