from binance.client import Client
import csv
import talib
from numpy import genfromtxt


client = Client('pldGqMhhqrwAFW6PVWr2uVQ4q83ZuUKyoZhHkO03JcwBnhvdSZsthkbR7YhVyPeZ', 'IoWeJtJjIhBTQXX8xeTThed06Vu7qaWU3r8sWaovv79JA184mK0zFTd6EhjqrGOF')
exchange_info = client.get_exchange_info()



# klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Dec, 2017")

# csvfile = open('allday_present.csv', 'w', newline='')
# kline_candlestick = csv.writer(csvfile, delimiter=',')

# for i in klines:
#     i[0] = i[0] / 1000
#     kline_candlestick.writerow(i)

# my_data = genfromtxt('2020-2021.csv', delimiter=',')

# close = my_data[:,4]

# real = talib.RSI(close, timeperiod=14)

# print(real) 