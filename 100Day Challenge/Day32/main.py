import smtplib
from dotenv import load_dotenv
import os

load_dotenv()
my_email = os.getenv("EMAIL")
my_password = os.getenv("EMAIL_PASSWORD")
test_email = os.getenv("TEST_EMAIL")
# making connection with the smpt
with smtplib.SMTP("smtp.gmail.com") as connection:
    # tls -> transport layer security, makes the connection secure
    connection.starttls()
    connection.login(my_email,my_password)

    connection.sendmail(from_addr=my_email, to_addrs= test_email,
                        msg="Subject:Subject\n\nHello this is testing mail")