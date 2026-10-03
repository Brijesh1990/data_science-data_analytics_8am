# create a canteen management app 
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

# create a data for canteen management app

data={
    "foodname":["pizza","burger","apple","gujrati thali","panjabi","south indian","chinease"],
    "quantity":[200,100,100,200,150,200,350],
    "wastage_food":[20,10,30,25,2,5,45]
}

# calculate in tabular layout  
df=pd.DataFrame(data)
print(df)
# total quantity of food
print('-----------------------------------------------')
total_food_qty=df["quantity"].sum()
print("total quantity of foods is :",total_food_qty,"kg")
#  total wastage items of food

print('-----------------------------------------------')
total_wastage_food=df["wastage_food"].sum()
print("total wastage  of foods is :",total_wastage_food,"kg")

# max in kg whick food is wastage 
print('-----------------------------------------------')
max_food_wasage=df["wastage_food"].max()
print("Maximum wastage food is :",max_food_wasage,"kg",df["foodname"][6])
# data visualization in graph 
plt.title("max food wasatage management")
# plt.xlabel(df["foodname"])
# plt.ylabel(df["wastage_food"])
plt.pie(
    df["wastage_food"], 
    labels=df["foodname"], 
    colors=["yellow","green","blue","coral","lightgray","green","red"],
    autopct="%1.1f%%"
)
# show chart
plt.show()

