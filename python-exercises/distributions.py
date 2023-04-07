from scipy.stats import norm
from scipy.stats import expon
from scipy.stats import binom
from scipy.stats import poisson
import matplotlib.pyplot as plt
import numpy as np

# Uniform dist
values = np.random.uniform(-10.0, 10.0, 100000)
plt.hist(values, 50)
plt.show()

# Gaussian
x = np.arange(-3, 3, 0.001)
plt.plot(x, norm.pdf(x))
plt.show

mu = 5.0
sigma = 2.0
values = np.random.normal(mu, sigma, 10000)
plt.hist(values, 50)
plt.show()

# Exponential PDF
x = np.arange(0, 10, 0.001)
plt.plot(x, expon.pdf(x))

#Binomial Probability Mass Functions
n, p = 10, 0.5
x = np.arange(0, 10, 0.001)
plt.plot(x, binom.pmf(x, n, p))

#Poisson Probability Mass Function
# Website gets average 500 visits/day. What's the odds of getting 550?
mu = 500
x = np.arange(400, 600, 0.5)
plt.plot(x, poisson.pmf(x, mu))