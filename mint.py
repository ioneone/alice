import settings
import mintapi
import os

MY_GMAIL_ADDRESS = os.getenv('MY_GMAIL_ADDRESS')
MINT_PASSWORD = os.getenv('MINT_PASSWORD')

mint = mintapi.Mint(MY_GMAIL_ADDRESS, MINT_PASSWORD)

print(mint.get_accounts())
