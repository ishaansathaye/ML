import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Part 1: Without numpy
# import csv
# x = []
# y= []
#
# #read from a csv file
# with open('example', 'r') as csvfile:
#     plots = csv.reader(csvfile, delimiter=',') #delimeter: things that data is spearated by
#     for row in plots:
#         x.append(int(row[0]))
#         y.append(int(row[1]))
#
# plt.plot(x, y, label='loaded from file')

# Part 2: Using numpy
# x, y = np.loadtxt('example', delimiter=',', unpack=True) #unpack: unpack the variables, only two variables
# plt.plot(x, y, label='loaded from file')

# Part 3: Using pandas
x = pd.read_csv('matplotlib/example', usecols=[0])
y = pd.read_csv('matplotlib/example', usecols=[1])
plt.plot(x, y, label='loaded from file')


plt.xlabel('X-Values')
plt.ylabel('Y-Values')
plt.title('Data\nCheck it out')

plt.legend()

plt.show()
