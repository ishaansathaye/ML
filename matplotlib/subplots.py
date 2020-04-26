import random
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()


def createPlots():
    xs = []
    ys = []

    for i in range(10):
        x = i
        y = random.randrange(10)

        xs.append(x)
        ys.append(y)
    return xs, ys


ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=1, colspan=1)
ax2 = plt.subplot2grid((6, 1), (1, 0), rowspan=4, colspan=1)
ax3 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1)

# add_subplot syntax: three graphs in one figure
# ax1 = fig.add_subplot(221)  # adding a plots inside of a figure
# ax2 = fig.add_subplot(222)
# ax3 = fig.add_subplot(212)


x, y = createPlots()
ax1.plot(x, y)

x, y = createPlots()
ax2.plot(x, y)

x, y = createPlots()
ax3.plot(x, y)

plt.show()
