import settings
import os
import requests
from notification import Client as NotificationClient
import gspread
from google.oauth2.service_account import Credentials
import json

ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
GOOGLE_SHEETS_CREDS_JSON = os.getenv('GOOGLE_SHEETS_CREDS_JSON')


class Client:

    def tick(self):
        creds_dict = json.loads(GOOGLE_SHEETS_CREDS_JSON)
        scopes = ['https://www.googleapis.com/auth/spreadsheets',
                  'https://www.googleapis.com/auth/drive']
        creds = Credentials.from_service_account_info(
            creds_dict, scopes=scopes)
        gc = gspread.authorize(creds)

        worksheet = gc.open("Personal Finance").sheet1
        list_of_lists = worksheet.get_all_values()
        columns = list_of_lists[0]
        rows = list_of_lists[1:]

        symbol_index = columns.index('symbol')
        last_price_index = columns.index('last price')

        price_cache = {}

        for index, row in enumerate(rows):
            symbol = row[symbol_index]

            if price_cache.get(symbol):
                last_price = price_cache[symbol]
            else:
                last_price = self.get_last_price(symbol)
                price_cache[symbol] = last_price

            range_name = chr(ord('A') + last_price_index) + str(2 + index)
            worksheet.update(range_name, last_price)

    def get_last_price(self, ticker: str):
        params = {
            'function': 'TIME_SERIES_DAILY',
            'symbol': ticker,
            'apikey': ALPHA_VANTAGE_API_KEY
        }

        response = requests.get(
            'https://www.alphavantage.co/query', params=params)
        response.raise_for_status()
        data = response.json()
        last_time_series = list(data['Time Series (Daily)'].values())[0]
        last_price = float(last_time_series['4. close'])
        return last_price


if __name__ == '__main__':
    client = Client()
    client.tick()
