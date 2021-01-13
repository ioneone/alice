import settings
import mintapi
import os

MY_GMAIL_ADDRESS = os.getenv('MY_GMAIL_ADDRESS')
MINT_PASSWORD = os.getenv('MINT_PASSWORD')

mint = mintapi.Mint(
    email=MY_GMAIL_ADDRESS,
    password=MINT_PASSWORD,
    mfa_method='email',
    headless=True
)

print(mint.get_accounts())
