import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mplfinance.original_flavor import candlestick_ohlc
import numpy as np
import urllib.request
from matplotlib import style

style.use('fivethirtyeight')
print(plt.style.available)

print(plt.__file__)


def bytespdate2num(b):
    return mdates.datestr2num(b.decode('utf-8'))


def graph_data(stock):
    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))

    stockPrice = 'https://pythonprogramming.net/yahoo_finance_replacement'
    sourceCode = urllib.request.urlopen(stockPrice).read().decode()
    stockData = []
    splitSource = sourceCode.split('\n')

    for line in splitSource[1:]:
        splitLine = line.split(',')
        if len(splitLine) == 7:
            if 'values' not in line and 'labels' not in line:
                stockData.append(line)

    date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stockData, delimiter=',', unpack=True,
                                                                      converters={0: bytespdate2num})
    x = 0
    y = len(date)
    ohlc = []

    while x < y:
        appendMe = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]
        ohlc.append(appendMe)
        x += 1

    candlestick_ohlc(ax1, ohlc, width=0.4, colorup='g', colordown='r')

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d-%Y'))
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax1.grid(True)

    bbox_props = dict(boxstyle = 'round4', fc='w', ec='k', lw=1) # adding annotation for last price
    ax1.annotate(str(closep[-1]), (date[-1], closep[-1]), xytext=(date[-1] + 4, closep[-1]), bbox=bbox_props)

    # annotation with arrows and text in graph
    # fontDict = {'family': 'serif', 'color': 'darkred', 'size': 15}  # font dictionary
    # ax1.text(date[20], closep[1], 'text example', fontdict=fontDict)  # putting text on the plot
    #
    # ax1.annotate('Good News', (date[11], highp[11]), xytext=(0.8, 0.9), textcoords='axes fraction',
    #              arrowprops=dict(facecolor='grey', color='grey'))
    # # annotation on the graph, fixes the annotation at the relative position, arrow moves

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(stock)
    # plt.legend()
    plt.subplots_adjust(left=0.11, bottom=0.24, right=0.90, top=0.90, wspace=0.2, hspace=0)
    plt.show()


graph_data('VZ')
