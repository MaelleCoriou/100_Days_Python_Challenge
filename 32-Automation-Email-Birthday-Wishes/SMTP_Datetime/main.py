# import smtplib
#
# my_email = "xxxx@gmail.com"
# password = "xxxx"
#
# # Connection to email provider server
# # Google search SMTP of provider to get the proper server name
# # Security account set up needs to be changed to low for gmail or a new password for app with Yahoo
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     # To secure connection encrypted
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     # Send email, to set up the subject of th email: msg="subject:text followed by \n\n message"
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="maellecoriou@yahoo.com",
#                         msg="Subject:Hello\n\nBody message")
#
#
# ## If connection not set up with "with ... as", connection needs to be closed:
# # connection = smtplib.SMTP("smtp.gmail.com")
# # ......
# # connection.close()

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
# 0=Monday 1=Tuesday...
day_of_week = now.weekday()
print(day_of_week)

# Create a new datetime object
birth_date = dt.datetime(year=1985, month=11, day=8, hour=3)
print(birth_date)
