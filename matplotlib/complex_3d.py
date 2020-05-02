from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d') # notify that the graphs is 3 dimensions

x, y, z = axes3d.get_test_data() # gives test data

print(axes3d.__file__)
ax1.plot_wireframe(x, y, z, rstride=5, cstride=5) #rstride and cstride creates distance

ax1.set_xlabel('X-Axis')
ax1.set_ylabel('Y-Axis')
ax1.set_zlabel('Z-Axis')
ax1.grid(True)

plt.show()