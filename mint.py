import settings
import mintapi
import os

MY_GMAIL_ADDRESS = os.getenv('MY_GMAIL_ADDRESS')
MY_GMAIL_PASSWORD = os.getenv('MY_GMAIL_PASSWORD')
MINT_PASSWORD = os.getenv('MINT_PASSWORD')

mint = mintapi.Mint(
    email=MY_GMAIL_ADDRESS,
    password=MINT_PASSWORD,
    mfa_method='email',
    imap_account=MY_GMAIL_ADDRESS,
    imap_password=MY_GMAIL_PASSWORD,
    imap_server='imap.gmail.com'
)

print(mint.get_accounts())
