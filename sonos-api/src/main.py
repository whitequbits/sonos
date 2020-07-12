import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from .stock import Stock
from .stock_symbol import StockSymbol
from .company import Company
from .stock_lstm_predictor import StockLSTMPredictor

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080"
]


HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}


def fastapi_app():
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get('/')
    def server_is_up():
        return 'server is up'

    @app.get('/stock_symbol')
    def get_stock_symbol():
      stock_symbol_data = StockSymbol().get_data()
      return stock_symbol_data

    @app.get('/company_data')
    def get_company_data(symbol):
      company_data = Company(symbol).get_data()
      return company_data

    @app.get('/stock_data')
    def get_stock_data(symbol):
      stock_data = Stock(symbol).get_data()
      return stock_data

    @app.get('/predict')
    def predict(symbol, future_day):
      future_day = int(future_day)
      stock_data = StockLSTMPredictor(symbol, future_day).predict()
      return stock_data

    @app.get('/stock_daily_data')
    def get_stock_daily_data(symbol):
      stock_data = Stock(symbol).get_daily_data()
      return stock_data

    return app


app = fastapi_app()

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8081)
