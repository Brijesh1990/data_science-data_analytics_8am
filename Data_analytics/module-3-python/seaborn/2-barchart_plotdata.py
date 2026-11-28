import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
# used seaborn barplot graph 
# sns: Seaborn library.
# load_dataset(): A function used to load an example dataset.
# "tips": The name of the dataset.
# tips: A variable that stores the dataset.

tips=sns.load_dataset("tips")
sns.barplot(x="total_bill", y="tip", data=tips)
#print(tips)
print(tips.head())
#print(tips.tail())
print(tips.shape)
# (244, 7)
# 244 = Total rows (records).
# 7 = Total columns (features).
# print only columns
print(tips.columns)

# create a statistical calculations 
# sum of total bills 
print("total sum of bills :",tips["total_bill"].sum())

# average a bill
print("total average of bills :",tips["total_bill"].mean())

# count total members 
print("total members  :",tips["sex"].count())

# max bills
print("Minimum  bills :",tips["total_bill"].min())

# min bills
print("Maximum   bills :",tips["total_bill"].max())

# show graph
plt.show()


