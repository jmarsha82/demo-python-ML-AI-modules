import numpy as np
import scipy.stats as sp
import matplotlib.pyplot as plt

vals = np.random.normal(0, 0.5, 10000)

plt.hist(vals, 50)
plt.show()

# moments are all about the shape of the distribution.  Variance, skew and kurtosis don't change if you change where the data is centered

# first moment is the mean
print(np.mean(vals))

# second moment is the variance
print(np.var(vals))

# third moment is the skew
print(sp.skew(vals))

# fourth moment is kurtosis
print(sp.kurtosis(vals))