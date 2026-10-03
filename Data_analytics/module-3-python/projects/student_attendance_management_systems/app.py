# create a student attendance management app
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# create a data for student attendance management app

data={
    "studentname":["Rahul","Priya","Amit","Neha","Karan","Pooja","Ravi"],
    "total_days":[100,100,100,100,100,100,100],
    "absent_days":[10,5,20,8,15,3,25]
}

# calculate in tabular layout
df=pd.DataFrame(data)
print(df)

# total attendance days
print('-----------------------------------------------')
total_days=df["total_days"].sum()
print("total attendance days is :",total_days)

# total absent days
print('-----------------------------------------------')
total_absent_days=df["absent_days"].sum()
print("total absent days of students is :",total_absent_days)

# maximum absent student
print('-----------------------------------------------')
max_student_absent=df["absent_days"].max()

# find student name who has maximum absence
max_absent_student=df.loc[df["absent_days"].idxmax(),"studentname"]

print("Maximum absent student is :",max_absent_student)
print("Maximum absent days is :",max_student_absent,"days")

# data visualization in graph
plt.title("Student Attendance Management - Maximum Absence")

# pie chart
plt.pie(
    df["absent_days"],
    labels=df["studentname"],
    colors=["yellow","green","blue","coral","lightgray","pink","red"],
    autopct="%1.1f%%"
)

# show chart
plt.show()
