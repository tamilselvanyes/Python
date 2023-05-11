import smtplib
from dotenv import load_dotenv
import os

load_dotenv()
# making connection with the smpt
connection = smtplib.SMTP("smtp.gmail.com")
# tls -> transport layer security, makes the connection secure
connection.starttls()
connection.login(os.getenv("EMAIL"), os.getenv("EMAIL_PASSWORD"))