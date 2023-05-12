import smtplib
from dotenv import load_dotenv
import os
import datetime as dt
from random import choice

load_dotenv()
my_email = os.getenv("EMAIL")
my_password = os.getenv("EMAIL_PASSWORD")
test_email = os.getenv("TEST_EMAIL")

now = dt.datetime.now()
day_of_week = now.weekday()

# date_of_birth = dt.datetime(year=1996, month=12, day=15, hour=5)
if day_of_week == 4:
    try:
        with open("quotes.txt") as quotes_data:
            data = quotes_data.readlines()
            stripped_data = [quote.strip() for quote in data]
            random_quote = choice(stripped_data)
            # making connection with the smpt
            with smtplib.SMTP("smtp.gmail.com") as connection:
                # tls -> transport layer security, makes the connection secure
                connection.starttls()
                connection.login(my_email, my_password)
                connection.sendmail(from_addr=my_email, to_addrs=test_email,
                                    msg=f"Subject:Monday Motivation\n\n{random_quote}")

    except FileNotFoundError:
        print("File not found")
