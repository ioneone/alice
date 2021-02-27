"""
Assume `python main.py` is executed every morning. 
"""

from weather import Client as WeatherClient
from notification import Client as NotificationClient
from stock import Client as StockClient
from datetime import date
from typing import Callable
import sys

notification_client = NotificationClient()
weather_client = WeatherClient()
stock_client = StockClient()


class TickManager:

    def __init__(self):
        self.ticks = []

    def add(self, name: str, tick: Callable[[], None]):
        self.ticks.append((name, tick))

    def run(self):
        for name, tick in self.ticks:
            try:
                tick()
            except:
                notification_client.send_email(
                    f"Tick Manager Error", f"Hi Junhong, something went wrong when running the job '{name}'")
                sys.stderr.write(
                    f"Tick Manager Error: something went wrong when running the job '{name}'")


tick_manager = TickManager()

tick_manager.add('check if it will rain today', weather_client.tick)
tick_manager.add('check S&P 500 performance', stock_client.tick)

tick_manager.run()
