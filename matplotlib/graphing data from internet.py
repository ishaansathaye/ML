import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import urllib.request as requests
import requests
from pandas_datareader import data, wb


# From tutorial (not working code)
# def bytespdate2num(fmt, encoding='utf-8'):
#     strconverter = mdates.strpdate2num(fmt)
#     def bytesconverter(b):
#         s = b.decode(encoding)
#         return strconverter(s)
#     return bytesconverter
#
# def graphData():
#
#     stockPriceURL = 'https://pythonprogramming.net/yahoo_finance_replacement'
#
#     #sourceCode = urllib.request.urlopen(stockPriceURL).read().decode()
#     sourceCode = requests.get(url=stockPriceURL, params=None, verify=False)
#
#     stockData = []
#     #splitSource = sourceCode.split('\n')
#     splitSource = sourceCode.json()
#
#     for line in splitSource:
#         splitLine = line.split(',')
#         if len(splitLine) == 7:
#             if 'Volume' not in line:
#                 stockData.append(line)
#
# date, openp, highp, lowp, closep, volume = np.loadtxt(stockData, delimiter=',', unpack=True, converters={0:
# bytespdate2num('%Y-%m-%d')})
#
#     plt.plot_date(date, closep)
#
#     plt.xlabel('date')
#     plt.ylabel('price')
#     plt.title('Stocks\nCheck it out')
#     plt.legend()
#     plt.show()

# Using pandas data reader import
# df = data.DataReader('TSLA','yahoo')
def graph_data(stock):
    df = data.DataReader(stock, data_source='yahoo')
    plt.plot_date(df.index, df.Close, '-', label='stock price')

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(stock + ' stock')
    plt.legend()
    plt.show()

stockName = input("What is the stock name: ")
graph_data(stockName)


