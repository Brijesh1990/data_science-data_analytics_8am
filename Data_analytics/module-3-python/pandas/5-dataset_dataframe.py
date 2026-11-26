import pandas as pd
import matplotlib.pyplot as plt
# create a data set 

data={
    "food":["paneer","flower","palak paneer","pizza","momoz","pani puri"],
    "wastage":[50,20,45,5,25,16]
}

# data frames create 
df=pd.DataFrame(data)
print(df)

# visualizations of data using matplolib
plt.figure(figsize=(8, 8))
plt.title("food wastage managements systems")
plt.pie(
    df["wastage"], 
    labels=df["food"],
    autopct="%1.1f%%", 
    startangle=90,
)


df=pd.DataFrame(data)
print(df["food"])
print(df["wastage"])

# total wastage 
print(df["wastage"].sum(), "kg")
# average wastage
print(df["wastage"].mean(), "kg")
# max wastage
print(df["wastage"].max(), "kg")
# min wastage
print(df["wastage"].min(), "kg")

plt.show()