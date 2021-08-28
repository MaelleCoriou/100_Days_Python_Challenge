import datetime as dt
from random import choice
import SMTP_Set_up
import pandas as pd

# Data
birthdays = pd.read_csv("birthdays.csv", encoding="UTF8 ")

# Today's date
now = dt.datetime.now()
month = now.month
day = now.day

# Find today's birthday
to_celebrate = [row for index, row in birthdays.iterrows() if row.month == month and row.day == day]
to_celebrate = pd.DataFrame(to_celebrate)
name = to_celebrate["name"].to_string(index=False)
email = to_celebrate["email"].to_string(index=False)

# Set letter
with open(file=f"letter_templates/letter_{choice(range(1,3))}.txt", mode="r", encoding="UTF8") as letter:
    wishes = letter.read()
    update_letter = wishes.replace("[NAME]", name)
    # Send letter calling send_email function
    SMTP_Set_up.send_email(message=f"subject:Happy birthday {name}\n\n{update_letter}", contact=f"{email}")


# -----> Finally setup PythonAnywhere to run the program everyday : https://www.pythonanywhere.com/user/MaelleCo/


# Angela's code:
#
# MY_EMAIL = "YOUR EMAIL"
# MY_PASSWORD = "YOUR PASSWORD"
#
# today = datetime.now()
# today_tuple = (today.month, today.day)
#
# data = pandas.read_csv("birthdays.csv")
# birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# if today_tuple in birthdays_dict:
#     birthday_person = birthdays_dict[today_tuple]
#     file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
#     with open(file_path) as letter_file:
#         contents = letter_file.read()
#         contents = contents.replace("[NAME]", birthday_person["name"])
#
#     with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=birthday_person["email"],
#             msg=f"Subject:Happy Birthday!\n\n{contents}"
#         )