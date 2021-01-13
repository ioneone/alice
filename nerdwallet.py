import settings
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from gmail import Client as GmailClient

MY_GMAIL_ADDRESS = os.getenv('MY_GMAIL_ADDRESS')
NERD_WALLET_PASSWORD = os.getenv('NERD_WALLET_PASSWORD')
SLEEP_SECONDS = 2


class Client:

    def check_net_worth(self):
        gmailClient = GmailClient()
        gmailClient.send("NerdWallet Login",
                         "Hey Junhong, I'm logging in to your NerdWallet account now "
                         "to keep track of your net worth. You may receive a "
                         "notification from NerdWallet about a new login. Please "
                         "ignore it.")

        browser = webdriver.Chrome(ChromeDriverManager().install())

        try:
            # Visit NerdWallet
            browser.get(
                'https://www.nerdwallet.com/home/signin?redirect_uri=/home/dashboard/home')
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

            print(f"Your net worth is {net_worth}")
        except:
            print(f"Unexpected error: {sys.exc_info()[0]}")
            gmailClient.send("NerdWallet client error", sys.exc_info()[0])

        browser.close()
