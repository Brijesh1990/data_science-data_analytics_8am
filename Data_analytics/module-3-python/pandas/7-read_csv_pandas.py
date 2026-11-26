import pandas as pd 
# read csv (comma seperated value)
# that can be read 5 start data and 5 end data 
# df=pd.read_csv("students_data.csv")
# print(df)

# head method read first start 5 data
# res=pd.read_csv("students_data.csv")
# df=res.head()
# print(df)

# end 5data only read 
# res=pd.read_csv("students_data.csv")
# df=res.tail()
# print(df)

# read only columns data
res=pd.read_csv("students_data.csv")
# df=res.tail()
# print(df["Full_Name"])

df=res.head()
print(df["Full_Name"])
# print(df["Full_Name"][0])

