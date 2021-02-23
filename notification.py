import os
import smtplib
import settings


MY_GMAIL_ADDRESS = os.getenv('MY_GMAIL_ADDRESS')
MY_PHONE_NUMBER = os.getenv('MY_PHONE_NUMBER')
BOT_GMAIL_ADDRESS = os.getenv('BOT_GMAIL_ADDRESS')
BOT_GMAIL_PASSWORD = os.getenv('BOT_GMAIL_PASSWORD')


class Client:

    def send_email(self, subject: str, body: str):
        """Sends a message to me as Alice via email"""
        self.send(MY_GMAIL_ADDRESS, subject, body)

    def send_sms(self, subject: str, body: str):
        """Sends a message to me as Alice via SMS"""
        self.send(f"{MY_PHONE_NUMBER}@tmomail.net", subject, body)

    def send(self, to_addrs: str, subject: str, body: str):
        """Sends a message to me as Alice."""
        header = f"From: Alice 🤖 <{BOT_GMAIL_ADDRESS}>\r\nTo: {to_addrs}\r\nSubject: {subject}"
        msg = f"{header}\r\n\r\n{body}".encode('utf8')

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=BOT_GMAIL_ADDRESS,
                             password=BOT_GMAIL_PASSWORD)
            connection.sendmail(from_addr=BOT_GMAIL_ADDRESS,
                                to_addrs=to_addrs,
                                msg=msg)
