import os
from dotenv import load_dotenv

load_dotenv()

FINNHUB_TOKEN = os.getenv("FINNHUB_TOKEN")
ALPHA_VANTAGE_TOKEN = os.getenv("ALPHA_VANTAGE_TOKEN")
