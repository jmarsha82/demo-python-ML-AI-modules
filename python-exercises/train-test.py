import numpy as np
from pylab import *
from sklearn.metrics import r2_score

np.random.seed(2)

pageSpeeds = np.random.normal(3.0, 1.0, 100)
purchaseAmount = np.random.normal(50.0, 30.0, 100) / pageSpeeds


scatter(pageSpeeds, purchaseAmount)
# plt.show()

trainX = pageSpeeds[:80] # First 80 go to training X
testX = pageSpeeds[80:] # Last 20 go to testing X

trainY = purchaseAmount[:80]
testY = purchaseAmount[80:]
scatter(testX, testY)

# plt.show()

x = np.array(trainX)
y = np.array(trainY)

p4 = np.poly1d(np.polyfit(x, y, 7)) # Fit our 8th degree polynomial

xp = np.linspace(0, 7, 100)
axes = plt.axes()
axes.set_xlim([0,7])
axes.set_ylim([0, 200])
plt.scatter(x, y)
plt.plot(xp, p4(xp), c='r')
# plt.show() # Show trend against data

testx = np.array(testX)
testy = np.array(testY)

axes = plt.axes()
axes.set_xlim([0,7])
axes.set_ylim([0, 200])
plt.scatter(testx, testy)
plt.plot(xp, p4(xp), c='r')
# plt.show() # Show trend again test data

r2 = r2_score(testy, p4(testx))

print(r2) # Test data

r2 = r2_score(np.array(trainY), p4(np.array(trainX)))

print(r2) # Train data
