from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from sklearn.metrics import mean_squared_error

class StockLstmModel:
  def __init__(self, look_back = 1):
    self.look_back = look_back

  def build_model(self):
    model = Sequential()
    model.add(LSTM(4, input_shape=(1, self.look_back)))
    model.add(Dropout(0.2))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')

    return model
