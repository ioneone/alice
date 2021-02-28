import os
import smtplib
import settings
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

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
        msg = MIMEMultipart()
        msg['From'] = BOT_GMAIL_ADDRESS
        msg['To'] = to_addrs
        msg['Subject'] = subject
        msg.attach(MIMEText(body))

        # Message through SMS Gateway is not properly encoded unless there are 2 or more MIME parts.
        msg.attach(MIMEText(''))

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=BOT_GMAIL_ADDRESS,
                             password=BOT_GMAIL_PASSWORD)
            connection.sendmail(from_addr=BOT_GMAIL_ADDRESS,
                                to_addrs=to_addrs,
                                msg=msg.as_string())


if __name__ == '__main__':
    client = Client()
    client.send_sms('subject 🙂', "Here is your tasty emoji: \U0001F31F")
    client.send_email('subject 🙂', 'Here is your tasty emoji: \U0001F31F')
