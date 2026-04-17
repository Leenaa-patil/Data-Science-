import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

datapath=pd.read_csv('data.csv')
# 1. cleaning raw data

print(datapath.head(5))
print("--------------------------------------------------------")
print(datapath.describe())
# drop duplicates
datapath.drop_duplicates(inplace=True)
# outliners
datapath = datapath[datapath['Calories'] < 1000]
datapath = datapath[datapath['Duration'] < 60]

meancal=datapath['Calories'].mean()
datapath.fillna({'Calories':meancal}, inplace=True)
# print(datapath.to_string())

# 2. visualization of data
datapath.plot(kind='scatter', x='Duration', y='Calories')
plt.title("Duration vs Calories Burned")
plt.xlabel("Duration (minutes)")
plt.ylabel("Calories")
plt.show()

sns.heatmap(datapath.corr(), annot=True)
plt.title("Correlation Between Variables")
plt.show()

datapath.boxplot(column=['Calories'])
plt.title("Calories Distribution (Boxplot)")

plt.show()

# 3. insights from data
print("\nInsights:")
print("1. Duration and calories have a positive relationship.")
print("2. Most workouts are within a limited duration range.")
print("3. Extreme values were removed for better accuracy.")

