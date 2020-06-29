import os
from flask import Flask, jsonify, request

import json
from stock import Stock
from stock_lstm_predictor import StockLSTMPredictor


HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}

def flask_app():
    app = Flask(__name__)


    @app.route('/', methods=['GET'])
    def server_is_up():
        return 'server is up'

    @app.route('/stock_data', methods=['GET'])
    def get_stock_data():
      symbol = request.args.get('symbol')
      stock_data = Stock(symbol).get_data()
      return stock_data

    @app.route('/predict', methods=['GET'])
    def predict():
      symbol = request.args.get('symbol')
      future_day = int(request.args.get('future_day'))
      stock_data = StockLSTMPredictor(symbol, future_day).predict()
      return stock_data

    return app

if __name__ == '__main__':
    app = flask_app()
    app.run(debug=True, host='0.0.0.0')
