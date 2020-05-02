from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d') # notify that the graphs is 3 dimensions

x = [1,2,3,4,5,6,7,8,9,10]
y = [6,6,7,8,2,5,6,3,7,2]
z = [1,2,6,3,2,7,3,3,7,2]

ax1.plot(x,y,z)
ax1.set_xlabel('X-Axis')
ax1.set_ylabel('Y-Axis')
ax1.set_zlabel('Z-Axis')
ax1.grid(True)

plt.show()
