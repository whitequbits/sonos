import requests
import json


class Company:
  def __init__(self, symbol):
    self.symbol = symbol

  def get_data(self):
    response = requests.get(
        f"https://finnhub.io/api/v1/stock/profile2?symbol={self.symbol}.JK&token=bs00m3vrh5renbkv7nk0")

    return response.json()
