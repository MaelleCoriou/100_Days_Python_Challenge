import smtplib
import os


# Get environment variables with password
EMAIL = os.environ.get('GMAIL_ADDRESS')
PASSWORD = os.environ.get('GMAIL_PASSWORD')


def send_email(message, contact):
    """ message: "subject:text followed by \n\n message
        contact: email address of destination"""
    # Connection to email provider server
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # To secure connection encrypted
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        # Send email, to set up the subject of th email: msg="subject:text followed by \n\n message"
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=contact,
                            msg=message)

