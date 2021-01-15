"""
Assume `python main.py` is executed every morning, 
"""

from weather import Client as WeatherClient
from nerdwallet import Client as NerdWalletClient
from gmail import Client as GmailClient
from datetime import date

gmailClient = GmailClient()

# Daily Tasks
try:
    weatherClient = WeatherClient()
    weatherClient.send_email_if_rain_today()
except:
    gmailClient.send("Weather Client Error",
                     "Hi Junhong, something went wrong when running WeatherClient.")

    # Monthly Tasks
if date.today().day == 1:
    try:
        nerdWalletClient = NerdWalletClient()
        nerdWalletClient.append_net_worth_entry()
    except:
        gmailClient.send("NerdWallet Client Error",
                         "Hi Junhong, something went wrong when running NerdWalletClient.")
