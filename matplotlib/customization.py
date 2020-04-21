import matplotlib.pyplot as plt
from pandas_datareader import data
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc


def graph_data(stock):
    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))  # first tuple: dimensions second tuple: start or origin

    df = data.DataReader(stock, data_source='yahoo')

    ax1.plot_date(df.index, df.Close, '-', label='stock price', color='b')

    ax1.plot([], [], linewidth=5, label='Loss', color='r', alpha=0.5)
    ax1.plot([], [], linewidth=5, label='Gain', color='g', alpha=0.5)

    ax1.fill_between(df.index, df.Close, df.Close[0], where=(df.Close > df.Close[0]), facecolor='g',
                     alpha=0.5)  # alpha: degree of transparency, between close and close[0] it fills
    ax1.fill_between(df.index, df.Close, df.Close[0], where=(df.Close < df.Close[0]), facecolor='r', alpha=0.5)

    ax1.set_facecolor('k')  # customizing the graph background color

    for label in ax1.xaxis.get_ticklabels():  # modifying labels to rotate
        label.set_rotation(45)

    ax1.grid(True, color='w', linestyle='-', linewidth=2)  # customizing the grid

    ax1.xaxis.label.set_color('g')  # setting the color of the axis labels
    ax1.yaxis.label.set_color('y')

    ax1.set_yticks([0, 25, 50, 75])  # settings the ticks on the y-axis or increment

    # axis customizations
    ax1.spines['left'].set_color('c')
    ax1.spines['bottom'].set_color('c')
    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)
    ax1.spines['left'].set_linewidth(5)
    ax1.spines['bottom'].set_linewidth(5)

    # ticks or numbers on axis customization
    ax1.tick_params(axis='x', colors='#f06215')

    # h-line
    ax1.axhline(df.Close[0], color='y', linewidth=5)

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(stock + ' stock')
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.93, wspace=0.2,
                        hspace=0)  # resizing the window for graph
    plt.show()


graph_data("VZ")
