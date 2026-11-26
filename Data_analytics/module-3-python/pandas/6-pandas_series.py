import pandas as pd
# create a data set 

data={
    "food":["paneer","flower","palak paneer","pizza","momoz","pani puri"],
    "wastage":[50,20,45,5,25,16]
}

# data frames create 
df=pd.Series(data)
print(df)
print(df["food"])
print(df["wastage"])
