import requests
import json
from . import settings

class Stock:
  def __init__(self, symbol):
    self.symbol = symbol

  def get_data(self):
    response = requests.get(
        f"https://finnhub.io/api/v1/stock/metric?symbol={self.symbol}.JK&metric=valuation&token={settings.FINNHUB_TOKEN}")

    return response.json()

  def get_daily_data(self):
    response = requests.get(
        f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={self.symbol}.JK&apikey={settings.ALPHA_VANTAGE_TOKEN}&outputsize=compact&datatype=json")

    return response.json()

