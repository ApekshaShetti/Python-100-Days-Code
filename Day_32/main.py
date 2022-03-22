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
import pandas
import random

MY_EMAIL = "apekshashetti1012@gmail.com"
MY_PASSWORD = "apeksha1000()"

now = dt.datetime.now()
today = (now.month,now.day)

dates = pandas.read_csv("Day_32/birthdays.csv")

birthdays_dict = {(data_row["month"],data_row["day"]): data_row for (index,data_row) in data.iterrows()}
if today in birthdays_dict:
    birthday_person = birthdays_dict[tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )


