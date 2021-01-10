import os
import smtplib
import settings
from gmail import Client as GmailClient
from weather import Client as WeatherClient

gmailClient = GmailClient()
weatherClient = WeatherClient()

if weatherClient.check_rain_today():
    gmailClient.send(
        "Rain Alert 🌧", "Hey, it will rain today. Don't forget to bring an umbrella! ☂️")
