from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
from pylab import randn
### XKCD STYLE ###
# plt.xkcd()

# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# plt.xticks([])
# plt.yticks([])
# ax.set_ylim([-30, 10])

# data = np.ones(100)
# data[70:] -= np.arange(30)

# plt.annotate(
#     'This is when\nI became an alcoholic',
#     xy=(70, 1), arrowprops=dict(arrowstyle='->'), xytext=(15, -10))

# plt.plot(data)

# plt.xlabel('time')
# plt.ylabel('my overall health')

### PIE CHART ###

# plt.rcdefaults()
# values = [12, 55, 4, 32, 14]
# colors = ['r', 'g', 'b', 'c', 'm']
# explode = [0, 0, 0.2, 0, 0]
# labels = ['India', 'United States', 'Russia', 'China', 'Europe']
# plt.pie(values, colors= colors, labels=labels, explode = explode)
# plt.title('Student Locations')

### BAR CHART ###

# values = [12, 55, 4, 32, 14]
# colors = ['r', 'g', 'b', 'c', 'm']
# plt.bar(range(0,5), values, color= colors)
# plt.show()

### SCATTER PLOT ###

X = randn(500)
Y = randn(500)
plt.scatter(X,Y)
plt.xlabel('Age')
plt.ylabel('Time Spent Watching TV')
plt.show()

### BOX AND WHISKER PLOT ###

# uniformSkewed = np.random.rand(100) * 100 - 40
# high_outliers = np.random.rand(10) * 50 + 100
# low_outliers = np.random.rand(10) * -50 - 100
# data = np.concatenate((uniformSkewed, high_outliers, low_outliers))
# plt.boxplot(data)
# plt.show()