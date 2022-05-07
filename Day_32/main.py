# Motivation quotes code

# from calendar import week
# import smtplib
# import datetime as dt
# import random

# MY_EMAIL = "apekshashetti1012@gmail.com"
# MY_PASSWORD = "apeksha1000()"

# now = dt.datetime.now()
# weekday = now.weekday()
# if weekday == 1:
#     with open("quotes.txt") as quote_file:
#         all_quotes = quote_file.readlines()
#         quote = random.choice(all_quotes)
    
#     print(quote)
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL,MY_PASSWORD)
#         connection.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL, msg=f"Subject: Monday Motivation\n\n{quote}")



# Automated Birthday Wisher

import smtplib
import datetime as dt
import pandas as pd
import random#To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )


MY_EMAIL = "shetti1012@gmail.com"
MY_PASSWORD = "Shetti1000"

now = dt.datetime.now()
today = (now.month,now.day)

dates = pd.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"],data_row["day"]): data_row for (index,data_row) in dates.iterrows()}
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]",birthday_person["name"])

with smtplib.SMTP("smtp.gmail.com",587) as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=birthday_person["email"],
        msg=f"Subject:Happy Birthday!\n\n{contents}"
    )

