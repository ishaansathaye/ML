import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([5,7,4,3,4,9,6,3,2,1])

m, b = np.polyfit(x, y, 1)

plt.scatter(x,y, label='Scattered Data', color='red', marker='x', s=100) # s = size, marker is type of sign

plt.plot(x, m*x + b) # line of best fit


plt.xlabel('X-Values')
plt.ylabel('Y-Values')
plt.title('Intro to Matplotlib\nCheck it out')

plt.legend()

plt.show()
