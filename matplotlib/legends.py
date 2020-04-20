#legends titles and labels
import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [5, 7, 4]
plt.plot(x, y, label="First Line")

x2 = [1, 2, 3]
y2 = [10, 14, 12]
plt.plot(x2, y2, label="Second Line")

plt.xlabel('X-Values')
plt.ylabel('Y-Values')
plt.title('Intro to Matplotlib\nCheck it out')

plt.legend()

plt.show()
