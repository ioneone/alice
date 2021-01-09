import os
import smtplib
import settings

MY_EMAIL_ADDRESS = os.getenv('MY_EMAIL_ADDRESS')
BOT_EMAIL_ADDRESS = os.getenv('BOT_EMAIL_ADDRESS')
BOT_EMAIL_PASSWORD = os.getenv('BOT_EMAIL_PASSWORD')

header = f"From: {BOT_EMAIL_ADDRESS}\r\nTo: {MY_EMAIL_ADDRESS}\r\nSubject: Heroku Scheduler Test"
body = "If you're receiving this email, then you have successfully configured Heroku Scheduler!"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=BOT_EMAIL_ADDRESS,
                     password=BOT_EMAIL_PASSWORD)
    connection.sendmail(from_addr=BOT_EMAIL_ADDRESS, to_addrs=MY_EMAIL_ADDRESS,
                        msg=f"{header}\r\n\r\n{body}".encode("utf8"))
