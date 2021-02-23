import settings
import os
import requests
from datetime import date, timedelta
from notification import Client as NotificationClient

ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')


class Client:

    def tick(self):
        percentage = self.get_percentage_diff_from_last_week()

        notification_client = NotificationClient()

        if percentage > 0:
            notification_client.send_email(
                f"S&P 500 Tracker +{abs(percentage)}% 👍", f"S&P 500 has increased by {abs(percentage)}% since last week")
        else:
            notification_client.send_email(
                f"S&P 500 Tracker -{abs(percentage)}% 👎", f"S&P 500 has decreased by {abs(percentage)}% since last week")

    def get_percentage_diff_from_last_week(self):
        params = {
            'function': 'TIME_SERIES_DAILY',
            'symbol': 'VOO',
            'apikey': ALPHA_VANTAGE_API_KEY
        }

        response = requests.get(
            'https://www.alphavantage.co/query', params=params)
        response.raise_for_status()
        data = response.json()
        time_series = data['Time Series (Daily)']

        yesterday = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
        last_week = (date.today() - timedelta(days=7)).strftime("%Y-%m-%d")

        price_yesterday = float(time_series[yesterday]['4. close'])
        price_last_week = float(time_series[last_week]['4. close'])

        diff = price_yesterday - price_last_week
        percentage = diff / price_last_week * 100

        return round(percentage, 2)


if __name__ == '__main__':
    client = Client()
    client.tick()
