import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("http://media.sundog-soft.com/SelfDriving/FuelEfficiency.csv")
gear_counts = df['# Gears'].value_counts()
# gear_counts.plot(kind='bar')
# plt.show()

### Changing appearance by adding seaborn

sns.set(color_codes=True)
# gear_counts.plot(kind='bar')
# plt.show()
print(df.head())
# sns.displot(df['CombMPG'], kde=True) # Bar chart with trend line
# plt.show()

df2 = df[['Cylinders', 'CityMPG', 'HwyMPG', 'CombMPG']]
# print(df2.head())

# sns.pairplot(df2, height=2.5)

# sns.scatterplot(x="Eng Displ", y="CombMPG", data=df)
# sns.jointplot(x="Eng Displ", y="CombMPG", data=df)
# sns.lmplot(x="Eng Displ", y="CombMPG", data=df)

sns.set(rc={'figure.figsize':(15,5)})
# ax=sns.boxplot(x='Mfr Name', y='CombMPG', data=df)
# ax.set_xticklabels(ax.get_xticklabels(),rotation=45)

# ax=sns.swarmplot(x='Mfr Name', y='CombMPG', data=df)
# ax.set_xticklabels(ax.get_xticklabels(),rotation=45)

# ax=sns.countplot(x='Mfr Name', data=df)
# ax.set_xticklabels(ax.get_xticklabels(),rotation=45)

df2 = df.pivot_table(index='Cylinders', columns='Eng Displ', values='CombMPG', aggfunc='mean')
sns.heatmap(df2)

sns.scatterplot(x="# Gears", y="CombMPG", data=df)
plt.show()
sns.lmplot(x="# Gears", y="CombMPG", data=df)
plt.show()
sns.jointplot(x="# Gears", y="CombMPG", data=df)
plt.show()
sns.boxplot(x="# Gears", y="CombMPG", data=df)
plt.show()
sns.swarmplot(x="# Gears", y="CombMPG", data=df)
plt.show()