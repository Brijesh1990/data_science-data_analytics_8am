import seaborn as sns 
import matplotlib.pyplot as plt


tips=sns.load_dataset("tips")
sns.scatterplot(
    x="total_bill",
    y="tip",
    data=tips
)

plt.title("Total Bill vs Tip")

print("total sum of bills :",tips["total_bill"].sum())

# average a bill
print("total average of bills :",tips["total_bill"].mean())

# count total members 
print("total members  :",tips["sex"].count())

# max bills
print("Minimum  bills :",tips["total_bill"].min())

# min bills
print("Maximum   bills :",tips["total_bill"].max())

plt.show()