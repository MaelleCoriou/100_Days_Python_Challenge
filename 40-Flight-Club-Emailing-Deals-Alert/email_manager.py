import smtplib
import os
 
    
# Get environment variables
EMAIL = os.environ.get("GMAIL_ADDRESS")
PASSWORD = os.environ.get("GMAIL_PASSWORD")


class EmailManager:

    def send_email(self, emails, message, google_flight_link):
        # Connection to email provider server
        with smtplib.SMTP("smtp.gmail.com") as connection:
            # To secure connection encrypted
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            for email in emails:
                # Send email, to set up the subject of th email: msg="subject:text followed by \n\n message"
                connection.sendmail(from_addr=EMAIL,
                                    to_addrs=email,
                                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}"
                                    )