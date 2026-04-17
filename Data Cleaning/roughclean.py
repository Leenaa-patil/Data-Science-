import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

datapath=pd.read_csv('data.csv')
# print(datapath)
# to drop missing values in place or in the same dataset=
# cleandata=datapath.dropna() = to create a new data set with clean values
datapath.dropna(inplace=True)
# to checck for duplicates
# print(datapath.duplicated())
# to delete duplicates
datapath.drop_duplicates(inplace=True)
# to get basic statistical information about the data
print(datapath.describe())
# to visualize data in line graph
datapath.plot()
plt.show()

# to visualize data in scatter plot
datapath.plot(kind='scatter', x='Duration', y='Calories')
plt.show()

sns.heatmap(datapath.corr(), annot=True)
plt.show()


