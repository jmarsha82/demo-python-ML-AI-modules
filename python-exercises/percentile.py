import numpy as np
import matplotlib.pyplot as plt

vals = np.random.normal(0, 0.75, 10000)

plt.hist(vals, 50)
plt.show()

print(np.percentile(vals, 50))
print(np.percentile(vals, 90))
print(np.percentile(vals, 20))