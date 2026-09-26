'''
bash
pip install pandas
or
pip show pandas 

python
import pandas as pd

'''

import pandas as pd 
import matplotlib.pyplot as plt
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
# visualized data in chart using matplotlib
'''
bash
pip install matplotlib
or
pip show matplotlib

python
import matplotlib.pyplot as plt

'''

# generate excel 
df[["name", "salary"]].to_excel("employee.xlsx", index=False)
print("Excel generated successfully")

# bar chart
# plt.title("Display data in  bar chart")
# plt.bar(df["name"],df["salary"])
# # print chart
# plt.show()

# pie chart
plt.title("Display data in  pie chart")
plt.pie(df["salary"],labels=df["name"], autopct="%1.1f%%")
# print chart
plt.show()