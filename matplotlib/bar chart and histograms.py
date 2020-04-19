import matplotlib.pyplot as plt

# Bar Charts #
# x = [2,4,6,8,10]
# y = [6,7,8,4,2]
#
# plt.bar(x, y, label="Bar Graph 1", color='blue')
#
# x2 = [1,3,5,7,9]
# y2 = [7,8,2,4,2]
#
# plt.bar(x2, y2, label="Bar Graph 2",color='k')

# Histograms
populationAges = [22, 55, 60, 45, 10, 21, 32, 99, 110, 120, 103, 17, 18 ,19, 65, 43, 48, 49, 50, 51, 57, 59, 31, 11, 117]
# ids = [x for x in range(len(populationAges))] *use for bar graphs

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(populationAges, bins, histtype='bar', rwidth=0.8)

plt.xlabel('X-Values')
plt.ylabel('Y-Values')
plt.title('Intro to Matplotlib\nCheck it out')

plt.legend()

plt.show()
