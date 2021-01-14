"""
Assume `python main.py` is executed every morning, 
"""

from weather import Client as WeatherClient
from nerdwallet import Client as NerdWalletClient
from datetime import date

# Daily Tasks
weatherClient = WeatherClient()
weatherClient.send_email_if_rain_today()

# Monthly Tasks
if date.today().day == 1:
    nerdWalletClient = NerdWalletClient()
    nerdWalletClient.check_net_worth()
