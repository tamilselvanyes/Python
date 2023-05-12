import smtplib
from dotenv import load_dotenv
import os
import datetime as dt

load_dotenv()
my_email = os.getenv("EMAIL")
my_password = os.getenv("EMAIL_PASSWORD")
test_email = os.getenv("TEST_EMAIL")
# making connection with the smpt
with smtplib.SMTP("smtp.gmail.com") as connection:
    # tls -> transport layer security, makes the connection secure
    now = dt.datetime.now()
    day_of_week = now.weekday()

    # date_of_birth = dt.datetime(year=1996, month=12, day=15, hour=5)
    if day_of_week == 4:
        connection.starttls()
        connection.login(my_email, my_password)
        try:
            with open("notes.txt") as quotes_data:
                data = quotes_data.readlines()
                print(data)
                for quote in data:
                    quote.strip()
                print(data)

            # connection.sendmail(from_addr=my_email, to_addrs= test_email,
            #                     msg="Subject:Subject\n\nHello this is testing mail")

        except FileNotFoundError:
            print("File not found")


