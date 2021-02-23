"""
Assume `python main.py` is executed every morning. 
"""

from weather import Client as WeatherClient
from notification import Client as NotificationClient
from stock import Client as StockClient
from datetime import date
from typing import Callable

notification_client = NotificationClient()
weather_client = WeatherClient()
stock_client = StockClient()


class TickManager:

    def __init__(self):
        self.ticks = []

    def add(tick: Callable[[], None]):
        self.tick.appned(tick)

    def run():
        for tick in self.ticks:
            try:
                tick()
            except:
                notification_client.send_email(
                    f"{name} Error", f"Hi Junhong, something went wrong when running the job '{tick.__name__}'")


tick_manager = TickManager()

tick_manager.add(weather_client.tick)
tick_manager.add(stock_client.tick)

tick_manager.run()
