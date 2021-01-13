"""
Assume `python main.py` is executed every morning, 
"""

from weather import Client as WeatherClient
from nerdwallet import Client as NerdWalletClient
from datetime import date

weatherClient = WeatherClient()
weatherClient.send_email_if_rain_today()

nerdWalletClient = NerdWalletClient()
nerdWalletClient.check_net_worth()
