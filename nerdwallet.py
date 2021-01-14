import settings
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from gmail import Client as GmailClient
import sys
import traceback

MY_GMAIL_ADDRESS = os.getenv('MY_GMAIL_ADDRESS')
NERD_WALLET_PASSWORD = os.getenv('NERD_WALLET_PASSWORD')
SLEEP_SECONDS = 2


class Client:
    """NerdWallet scraper."""

    def check_net_worth(self):
        gmailClient = GmailClient()
        gmailClient.send("NerdWallet Login",
                         "Hey Junhong, I'm logging in to your NerdWallet account now "
                         "to keep track of your net worth. You may receive a "
                         "notification from NerdWallet about a new login. Please "
                         "ignore it.")

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

        try:
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

            net_worth = browser.find_element_by_tag_name('h4').text

        except:
            traceback.print_exc()
            gmailClient.send("NerdWallet Client Error",
                             f"Unexpected error: {sys.exc_info()[0]}\nYour NerdWallet scraper may be outdated.")
        else:
            print(f"Your net worth is {net_worth}")
        finally:
            browser.close()
