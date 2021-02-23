import settings
import os
import requests
from notification import Client as NotificationClient

OPEN_WEATHER_MAP_API_KEY = os.getenv('OPEN_WEATHER_MAP_API_KEY')
LOS_ANGELES_LATITUDE = 34.052235
LOS_ANGELES_LONGITUDE = -118.243683


class Client:

    def tick(self):
        if not self.check_rain_today():
            return

        notification_client = NotificationClient()
        notification_client.send_email(
            "Rain Alert 🌧", "Hey, it will rain today. Don't forget to bring an umbrella! ☂️")

    def check_rain_today(self):
        """Check if it will rain today."""
        hourly_forecast = self.get_hourly_forecast()
        # only care about next 12 hours
        hourly_forecast = hourly_forecast[:12]
        # weather conditions smaller than 700 mean rain, snow, storm, etc
        return any(hourly['weather'][0]['id'] < 700 for hourly in hourly_forecast)

    def get_hourly_forecast(self):
        """Get hourly forecast data of Los Angeles for the next 48 hours."""
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/onecall?lat={LOS_ANGELES_LATITUDE}&lon={LOS_ANGELES_LONGITUDE}&exclude=current,minutely,daily,alerts&appid={OPEN_WEATHER_MAP_API_KEY}")
        response.raise_for_status()
        data = response.json()
        return data['hourly']


if __name__ == '__main__':
    client = Client()
    client.tick()
