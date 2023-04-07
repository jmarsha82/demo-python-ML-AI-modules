import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(100.0, 20.0, 10000)
print(np.median(incomes))
print(np.mean(incomes))

plt.hist(incomes, 50)
plt.show()

incomes = np.append(incomes, [1000000000])

print(np.median(incomes))
print(np.mean(incomes))