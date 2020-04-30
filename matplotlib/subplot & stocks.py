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

MA1 = 10
MA2 = 30

def highMinusLow(high, low):
    return high-low


def movingAverage(value, window):
    weights = np.repeat(1.0, window)/window
    smas = np.convolve(value, weights, 'valid')
    return smas


def bytespdate2num(b):
    return mdates.datestr2num(b.decode('utf-8'))


def graph_data(days):
    fig = plt.figure()
    # ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=1, colspan=1)
    plt.title('Stock Info')
    ax2 = plt.subplot2grid((6, 1), (1, 0), rowspan=4, colspan=1)
    plt.xlabel('Date')
    plt.ylabel('Price')
    # ax3 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1)

    stockPrice = 'https://pythonprogramming.net/yahoo_finance_replacement'
    sourceCode = urllib.request.urlopen(stockPrice).read().decode()
    stockData = []
    splitSource = sourceCode.split('\n')

    intDays = int(days)

    for line in splitSource[1:(intDays+1)]:
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

    ma1 = movingAverage(closep, MA1)
    ma2 = movingAverage(closep, MA2)
    start = len(date[MA2-1:])

    h_l = list(map(highMinusLow, highp, lowp))

    # ax1.plot_date(date, h_l, '-')

    candlestick_ohlc(ax2, ohlc, width=0.4, colorup='g', colordown='r')

    for label in ax2.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d-%Y'))
    ax2.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax2.grid(True)

    bbox_props = dict(boxstyle='round', fc='w', ec='k', lw=1)  # adding annotation for last price
    ax2.annotate(str(closep[0]), (date[0], closep[0]), xytext=(date[0] + 1, closep[0]), bbox=bbox_props, fontsize='x-small')

    # annotation with arrows and text in graph
    # fontDict = {'family': 'serif', 'color': 'darkred', 'size': 15}  # font dictionary
    # ax2.text(date[20], closep[1], 'text example', fontdict=fontDict)  # putting text on the plot
    #
    # ax2.annotate('Good News', (date[11], highp[11]), xytext=(0.8, 0.9), textcoords='axes fraction',
    #              arrowprops=dict(facecolor='grey', color='grey'))
    # # annotation on the graph, fixes the annotation at the relative position, arrow moves


    # ax3.plot(date[-start:], ma1[-start:])
    # ax3.plot(date[-start:], ma2[-start:])


    # plt.legend()
    plt.subplots_adjust(left=0.11, bottom=0.24, right=0.85, top=0.90, wspace=0.2, hspace=0)
    plt.show()

graph_data(days=input('How many days of stock history?: '))
