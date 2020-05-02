from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d') # notify that the graphs is 3 dimensions

x = [1,2,3,4,5,6,7,8,9,10]
y = [6,6,7,8,2,5,6,3,7,2]
z = [1,2,6,3,2,7,3,3,7,2]

x2 = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
y2 = [-6,-6,-7,-8,-2,-5,-6,-3,-7,-2]
z2 = [-1,-2,-6,-3,-2,-7,-3,-3,-7,-2]

ax1.scatter(x,y,z, c='g', marker='o')
ax1.scatter(x2, y2, z2, c='r', marker='*')

ax1.set_xlabel('X-Axis')
ax1.set_ylabel('Y-Axis')
ax1.set_zlabel('Z-Axis')
ax1.grid(True)

plt.show()
