import pandas
import datetime as dt
import smtplib
from random import choice
from dotenv import load_dotenv
import os

load_dotenv()
my_email = os.getenv("EMAIL")
my_password = os.getenv("EMAIL_PASSWORD")
test_email = os.getenv("TEST_EMAIL")

letter_files = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']


def send_email(to_email, body):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # tls -> transport layer security, makes the connection secure
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email,
                            msg=f"Subject:Birthday Wished\n\n{body}")


def get_mail_content(name):
    with open(f"./letter_templates/{choice(letter_files)}") as template:
        letter_content = template.read()
        updated_content = letter_content.replace("[NAME]", name)
        return updated_content


try:
    now = dt.datetime.now()
    date = now.day
    month = now.month

    data = pandas.read_csv("./birthdays.csv")
    data_dict = data.to_dict(orient="records")

    for person in data_dict:
        print(person["day"], date)
        if person["month"] == month and person["day"] == date:
            content = get_mail_content(person["name"])
            send_email(person["email"], content)


except FileNotFoundError:
    print("Data file not found")


