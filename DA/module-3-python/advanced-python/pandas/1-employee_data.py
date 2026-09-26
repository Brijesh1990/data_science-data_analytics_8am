'''
bash
pip install pandas
or
pip show pandas 

python
import pandas as pd

'''

import pandas as pd 
# create a employee data 
employee={
    "name":["om","nimavat","aryan","brijesh","amish","mishri"],
    "age":[21,25,19,35,30,20],
    "salary":[21000,30000,18500,115000,45000,14500]
}

# create a data frames 
df=pd.DataFrame(employee)
print(df)
print("------------------------")
print("sum of salary :",df["salary"].sum());