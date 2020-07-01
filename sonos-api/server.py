import uvicorn
from fastapi import FastAPI
from stock import Stock
from stock_lstm_predictor import StockLSTMPredictor


HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}

def fastapi_app():
    app = FastAPI()

    @app.get('/')
    def server_is_up():
        return 'server is up'

    @app.get('/stock_data')
    def get_stock_data(symbol):
      stock_data = Stock(symbol).get_data()
      return stock_data

    @app.get('/predict')
    def predict(symbol, future_day):
      future_day = int(future_day)
      stock_data = StockLSTMPredictor(symbol, future_day).predict()
      return stock_data

    return app

if __name__ == '__main__':
    app = fastapi_app()
    uvicorn.run(app, host="127.0.0.1", port=8081)
