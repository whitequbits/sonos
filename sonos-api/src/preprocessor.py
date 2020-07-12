import pandas as pd
import numpy as np
import math
from sklearn.model_selection import train_test_split


def reshape_data(dataset, look_back = 1):
  dataX, dataY = create_dataset(dataset, look_back)

  return dataX, dataY


def create_dataset(dataset, look_back=1):
    dataX, dataY = [], []
    for i in range(len(dataset)-look_back-1):
        a = dataset[i:(i+look_back), 0]
        dataX.append(a)
        dataY.append(dataset[i + look_back, 0])

    return np.array(dataX), np.array(dataY)

def split_dataset(data):
  # split into train and test sets
  train, test = train_test_split(data, shuffle=False)
  train, test = np.asarray(train), np.asarray(test)
  return train, test

def convert_response(data):
    # convert the response into datetimerecords that can be
    # parsed by Pandas
    # counter is used to skip 5 first data
    counter = 0
    for date_time, value in data['Time Series (Daily)'].items():
        if counter > 4:
            r = {'datetime': date_time}
            r.update(value)
            yield r

        counter += 1


def convert_to_numeric(data, columns=['Open', 'High', 'Low', 'Close']):

  for column in columns:
    data[column] = pd.to_numeric(data[column])

  return data


def df_from_response(data,
                     columns=['Open', 'High', 'Low', 'Close']):

    # pass your response 'page'
    df = pd.DataFrame(convert_response(data))
    # rename the columns
    df = df.rename(columns={'1. open': 'Open',
                            '2. high': 'High',
                            '3. low': 'Low',
                            '4. close': 'Close'})
    df['datetime'] = pd.to_datetime(df['datetime'])
    df.set_index('datetime', inplace=True)
    df.sort_index(inplace=True)
    # extract the default columns
    df = df[columns]
    df = convert_to_numeric(df)
    return df
