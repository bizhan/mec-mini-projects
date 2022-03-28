# get api key from your .env file
import os
from dotenv import load_dotenv  # if missing this module, simply run `pip install python-dotenv`

load_dotenv()
API_KEY = os.getenv('NASDAQ_API_KEY')

print(API_KEY)
