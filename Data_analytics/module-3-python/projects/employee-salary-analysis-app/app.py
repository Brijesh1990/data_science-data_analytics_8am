# import all libraries 
import pandas as pd
import matplotlib.pyplot as plt

# create a data 
data={
    'Name': ['om', 'aryan', 'giriraj', 'amish','brijesh','astha','prit','sneha','lokesh'],
    'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65],
    'salary': [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000]
}
# create a tabular layout
df=pd.DataFrame(data)
print(df)

# print the data in tabular format
print(df.to_string(index=False))

# print total sum of salary
print('------------------------------')
sum_salary=df['salary'].sum()
print("Total sum of salary:", sum_salary)

# print the average salary
print('------------------------------')
avg_salary=df['salary'].mean()
print("Average salary:", avg_salary)

# create a bar chart to display those employees whose salary is greater than average salary
print('------------------------------')
plt.figure(figsize=(10, 6))
plt.title('Employees with Salary Greater than Average Salary')
# change all color of bar chart to gray
color = ['gray' if salary >= avg_salary else 'red' for salary in df['salary']]

plt.bar(df['Name'][df['salary']>=avg_salary], df['salary'][df['salary']>=avg_salary], color=color)

plt.xlabel('Name')
plt.ylabel('Salary')

# create all in line chart to display those employees whose salary is greater than average salary
# plt.figure(figsize=(10, 6))
# plt.title('Employees with Salary Greater than Average Salary')
# plt.plot(df['Name'][df['salary']>=avg_salary], df['salary'][df['salary']>=avg_salary], marker='o', color='blue')

# plt.xlabel('Name')  
# plt.ylabel('Salary')

# create a pie chart to display those employees whose salary is greater than average salary

# plt.figure(figsize=(8, 8))
# plt.title('Employees with Salary Greater than Average Salary')
# plt.pie(df['salary'][df['salary']>=avg_salary], labels=df['Name'][df['salary']>=avg_salary], autopct='%1.1f%%', startangle=90)

# # color of pie chart
# colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6','#c2f0c2','#ff6666']
# plt.pie(df['salary'][df['salary']>=avg_salary], labels=df['Name'][df['salary']>=avg_salary], autopct='%1.1f%%', startangle=90, colors=colors)

plt.show()
