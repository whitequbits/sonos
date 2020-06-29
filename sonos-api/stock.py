import requests

class Stock:
  def __init__(self, symbol):
    self.symbol = symbol

  def get_data(self):
    response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={self.symbol}.JK&apikey=MWS5CUQWP4SDJK9L&outputsize=compact&datatype=json")

    return response.json()

