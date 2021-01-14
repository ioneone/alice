import os
import smtplib
import settings

MY_GMAIL_ADDRESS = os.getenv('MY_GMAIL_ADDRESS')
BOT_GMAIL_ADDRESS = os.getenv('BOT_GMAIL_ADDRESS')
BOT_GMAIL_PASSWORD = os.getenv('BOT_GMAIL_PASSWORD')


class Client:

    def send(self, subject: str, body: str):
        """Sends an email to me as Alice."""
        header = f"From: Alice (bot) <{BOT_GMAIL_ADDRESS}>\r\nTo: {MY_GMAIL_ADDRESS}\r\nSubject: {subject}"
        msg = f"{header}\r\n\r\n{body}".encode('utf8')

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=BOT_GMAIL_ADDRESS,
                             password=BOT_GMAIL_PASSWORD)
            connection.sendmail(from_addr=BOT_GMAIL_ADDRESS,
                                to_addrs=MY_GMAIL_ADDRESS,
                                msg=msg)
