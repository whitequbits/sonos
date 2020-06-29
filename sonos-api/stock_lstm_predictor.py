from preprocessor import df_from_response, split_dataset, reshape_data
from stock import Stock
from stock_lstm_model import StockLstmModel
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd

class StockLSTMPredictor:
  def __init__(self, symbol, future_day=5):
    self.symbol = symbol
    self.future_day = future_day
    self.stock_dataset = Stock(self.symbol).get_data()

  def predict(self):
    # Preprocessing
    self.stock_dataset = df_from_response(self.stock_dataset)
    stock_dataset = self.stock_dataset.reset_index(drop=True)
    stock_dataset['prediction'] = stock_dataset['Close'].shift(-self.future_day)
    stock_dataset = stock_dataset.dropna()
    scaler = MinMaxScaler(feature_range=(0, 1))
    stock_dataset = scaler.fit_transform(stock_dataset)
    train_dataset, test_dataset = split_dataset(stock_dataset)
    trainX, trainY = reshape_data(train_dataset)
    trainX = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))

    # Model Building
    model = StockLstmModel().build_model()
    model.fit(trainX, trainY, epochs=50, batch_size=1, verbose=0)
    scale = MinMaxScaler()
    scale.min_, scale.scale_ = scaler.min_[3], scaler.scale_[3]

    # Prediction
    current_prediction_dataset = scaler.fit_transform(self.stock_dataset)
    current_prediction_dataset = np.asarray(current_prediction_dataset)
    current_prediction_datasetX, current_prediction_datasetY = reshape_data(current_prediction_dataset)
    current_prediction_datasetX = np.reshape(current_prediction_datasetX, (current_prediction_datasetX.shape[0], 1, current_prediction_datasetX.shape[1]))
    result = model.predict(current_prediction_datasetX)
    result = scale.inverse_transform(result)
    result = pd.DataFrame(data=result[~self.future_day:], columns=[f"{self.future_day}-day result"])

    return result.to_json()
    

  





