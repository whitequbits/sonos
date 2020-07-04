import requests
import json


class StockSymbol:
  def get_data(self):
    response = requests.get(
        f"https://finnhub.io/api/v1/stock/symbol?exchange=JK&token=bs00m3vrh5renbkv7nk0")

    return response.json()
