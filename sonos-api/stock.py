import requests
import json

class Stock:
  def __init__(self, symbol):
    self.symbol = symbol

  def get_data(self):
    response = requests.get(
        f"https://finnhub.io/api/v1/stock/metric?symbol={self.symbol}.JK&metric=valuation&token=bs00m3vrh5renbkv7nk0")

    return response.json()

