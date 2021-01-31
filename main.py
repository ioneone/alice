"""
Assume `python main.py` is executed every morning. 
"""

from weather import Client as WeatherClient
from nerdwallet import Client as NerdWalletClient
from gmail import Client as GmailClient
from datetime import date
from typing import Callable

gmailClient = GmailClient()
weatherClient = WeatherClient()
nerdWalletClient = NerdWalletClient()


def tick(name: str, task: Callable[[], None], condition: bool):
    if not condition:
        return

    try:
        task()
    except:
        gmailClient.send(
            f"{name} Error", f"Hi Junhong, something went wrong when running the task '{name}'")


# Daily Tasks
tick("Check Rain Today", weatherClient.send_email_if_rain_today, True)
