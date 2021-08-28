import smtplib
import datetime as dt
from random import choice
import os
import pw


# Set environment variables
pw.os_variable()

# Get environment variables
EMAIL = os.getenv('GMAIL_ADDRESS')
PASSWORD = os.environ.get('GMAIL_PASSWORD')


def send_email(message):
    # Connection to email provider server
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # To secure connection encrypted
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        # Send email, to set up the subject of th email: msg="subject:text followed by \n\n message"
        connection.sendmail(from_addr=EMAIL,
                            to_addrs="maellecoriou@yahoo.com",
                            msg=message)


now = dt.datetime.now()
day_of_week = now.weekday()

with open(file="quotes.txt") as file:
    data = file.readlines()

    if day_of_week == 5:
        quote = choice(data)
        send_email(message=f"Subject:Quote\n\n{quote}")
        print(quote)

