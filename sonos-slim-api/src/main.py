import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from .stock import Stock
from .stock_symbol import StockSymbol
from .company import Company
from .stock_lstm_predictor import StockLSTMPredictor
from .request_body import StockDetectionRequest
from .response_body import StockDetectionResponse

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080"
]


HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}


def fastapi_app():
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get('/')
    def server_is_up():
        return 'server is up'

    @app.post('/predict', response_model=StockDetectionResponse)
    def post_stock_detection(request_body: StockDetectionRequest):
      future_day = int(request_body.future_day)
      symbol = request_body.symbol
      stock_data = StockLSTMPredictor(symbol, future_day).predict()
      response = StockDetectionResponse(result=stock_data)
      return response

    return app


app = fastapi_app()

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8081)
