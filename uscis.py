import settings
import os
import requests
from notification import Client as NotificationClient
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options

USCIS_RECEIPT_NUMBER = os.getenv('USCIS_RECEIPT_NUMBER')


class Client:

    def __init__(self):
        options = Options()

        # these are the options automatically applied to heroku chrome driver
        options.add_argument('--disable-gpu')
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')

        options.add_argument(
            "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36")

        self.driver = webdriver.Chrome(
            ChromeDriverManager().install(), options=options)

        # Some element sizes become 0 in headless mode.
        # Explicitly set the window size to prevent that.
        self.driver.set_window_size(1440, 900)

    def send_status(self):
        status = self.get_status()
        notificationClient = NotificationClient()
        notificationClient.send_sms("OPT EAD Status", status)

    def get_status(self):
        self.driver.get('https://egov.uscis.gov/casestatus/landing.do')

        time.sleep(2)

        self.driver.find_element_by_id(
            'receipt_number').send_keys(USCIS_RECEIPT_NUMBER)

        self.driver.find_element_by_name('initCaseSearch').click()

        time.sleep(2)

        return self.driver.find_element_by_xpath('/html/body/div[2]/form/div/div[1]/div/div/div[2]/div[3]/h1').text


if __name__ == '__main__':
    client = Client()
    print(client.get_status())
