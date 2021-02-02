"""
Assume `python main.py` is executed every morning. 
"""

from weather import Client as WeatherClient
from notification import Client as NotificationClient
from uscis import Client as USCISClient
from datetime import date
from typing import Callable

notificationClient = NotificationClient()
weatherClient = WeatherClient()
uscisClient = USCISClient()


def tick(task: Callable[[], None]):
    try:
        task()
    except:
        notificationClient.send_sms(
            f"{name} Error", f"Hi Junhong, something went wrong when running the function '{task.__name__}'")


tick(weatherClient.send_sms_if_rain_today)
tick(uscisClient.send_status)
