import settings
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from gmail import Client as GmailClient
import sys
import traceback
import requests
from datetime import date

MY_GMAIL_ADDRESS = os.getenv('MY_GMAIL_ADDRESS')
NERD_WALLET_PASSWORD = os.getenv('NERD_WALLET_PASSWORD')
SHEETY_TOKEN = os.getenv('SHEETY_TOKEN')
SHEETY_API_ENDPOINT = os.getenv('SHEETY_API_ENDPOINT')
SHEETY_NET_WORTH_TRACKER_SHEET_ID = os.getenv(
    'SHEETY_NET_WORTH_TRACKER_SHEET_ID')

SLEEP_SECONDS = 2


class Client:

    def append_net_worth_entry(self):
        net_worth = self.get_net_worth()

        headers = {
            'Authorization': f"Bearer {SHEETY_TOKEN}"
        }
        json = {
            SHEETY_NET_WORTH_TRACKER_SHEET_ID: {
                'date': date.today().strftime("%m/%d/%Y"),
                'netWorth': net_worth
            }
        }
        response = requests.post(
            f"{SHEETY_API_ENDPOINT}/{SHEETY_NET_WORTH_TRACKER_SHEET_ID}", headers=headers, json=json)
        response.raise_for_status()

    def notify_login(self):
        """
        Sends an email to me to tell me not to worry about
        a new login from unrecognized device because every
        time a tick runs, it is a new device.
        """
        gmailClient = GmailClient()
        gmailClient.send("NerdWallet Login",
                         "Hey Junhong, I'm logging in to your NerdWallet account now "
                         "to keep track of your net worth. You may receive a "
                         "notification from NerdWallet about a new login. Please "
                         "ignore it.")

    def get_net_worth(self):
        """Get my current net worth from my NerdWallet account."""
        self.notify_login()

        options = Options()

        # these are the options automatically applied to heroku chrome driver
        options.add_argument('--disable-gpu')
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')

        # pretend to be a human
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")

        browser = webdriver.Chrome(
            ChromeDriverManager().install(), options=options)

        # Some element sizes become 0 in headless mode.
        # Explicitly set the window size to prevent that.
        browser.set_window_size(1440, 900)

        # Visit NerdWallet
        browser.get('https://www.nerdwallet.com/home/signin')
        time.sleep(SLEEP_SECONDS)

        # Login to my NerdWallet account
        browser.find_element_by_id(
            'my-nerdwallet-1-3').send_keys(MY_GMAIL_ADDRESS)
        browser.find_element_by_id(
            'my-nerdwallet-1-4').send_keys(NERD_WALLET_PASSWORD)

        browser.find_element_by_xpath("//button[@type='submit']").click()

        time.sleep(SLEEP_SECONDS)

        # Visit net worth page
        browser.get('https://www.nerdwallet.com/home/dashboard/net-worth')
        time.sleep(SLEEP_SECONDS)

        # e.g. "$20,000"
        net_worth = browser.find_element_by_tag_name('h4').text

        # e.g. 20000
        net_worth = int(net_worth.replace('$', '').replace(',', ''))

        browser.close()

        return net_worth
