import settings
import os
import requests
from datetime import date, timedelta
from notification import Client as NotificationClient

ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')


class Client:

    def tick(self):
        percentage_week, percetage_month = self.get_percentage_diffs()

        notification_client = NotificationClient()
        notification_client.send_sms(
            f"S&P 500 Tracker 👀", f"The price is {self.to_signed_str(percentage_week)}% from last week and {self.to_signed_str(percetage_month)} from last month.")

    def to_signed_str(self, val):
        if val > 0:
            return f"+{val}"
        else:
            return f"{val}"

    def get_percentage_diffs(self):
        params = {
            'function': 'TIME_SERIES_DAILY',
            'symbol': 'VOO',
            'apikey': ALPHA_VANTAGE_API_KEY
        }

        response = requests.get(
            'https://www.alphavantage.co/query', params=params)
        response.raise_for_status()
        data = response.json()
        time_series = list(data['Time Series (Daily)'].values())

        price_yesterday = float(time_series[0]['4. close'])
        price_last_week = float(time_series[6]['4. close'])
        price_last_month = float(time_series[29]['4. close'])

        diff_week = price_yesterday - price_last_week
        percentage_week = diff_week / price_last_week * 100

        diff_month = price_yesterday - price_last_month
        percentage_month = diff_month / price_last_month * 100

        return round(percentage_week, 2), round(percentage_month, 2)


if __name__ == '__main__':
    client = Client()
    client.tick()
