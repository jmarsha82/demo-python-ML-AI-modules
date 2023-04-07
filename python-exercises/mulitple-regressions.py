import pandas as pd
from pylab import *
import numpy as np
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pd.read_excel('http://cdn.sundog-soft.com/Udemy/DataScience/cars.xls')
df1=df[['Mileage','Price']]
bins =  np.arange(0,50000,10000)
groups = df1.groupby(pd.cut(df1['Mileage'],bins)).mean()
print(groups.head())
groups['Price'].plot.line()
plt.show()

X = df[['Mileage', 'Cylinder', 'Doors']]
y = df['Price']

X[['Mileage', 'Cylinder', 'Doors']] = scale.fit_transform(X[['Mileage', 'Cylinder', 'Doors']].values)

# Add a constant column to our model so we can have a Y-intercept
X = sm.add_constant(X)

print (X)

est = sm.OLS(y, X).fit()

print(est.summary())

print(y.groupby(df.Doors).mean())

scaled = scale.transform([[45000, 8, 4]])
scaled = np.insert(scaled[0], 0, 1) #Need to add that constant column in again.
print(scaled)
predicted = est.predict(scaled)
print(predicted)