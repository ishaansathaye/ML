from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

style.use('seaborn-white')
print(plt.style.available)

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d') # notify that the graphs is 3 dimensions

x3 = [1,2,3,4,5,6,7,8,9,10]
y3 = [6,6,7,8,2,5,6,3,7,2]
z3 = np.zeros(10) # want the bar chart to be on the ground (start z-axis at 0)

# depth value of each of the bars
dx = np.ones(10)
dy = np.ones(10)
dz = [1,2,3,4,5,6,7,8,9,10]

ax1.bar3d(x3, y3, z3, dx, dy, dz)

ax1.set_xlabel('X-Axis')
ax1.set_ylabel('Y-Axis')
ax1.set_zlabel('Z-Axis')
ax1.grid(True)

plt.show()