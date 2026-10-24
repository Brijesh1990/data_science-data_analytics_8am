import matplotlib.pyplot as plt 
import pandas as pd
import openpyxl
# create a database via sqlite3
import sqlite3
# create a database 
conn=sqlite3.connect("employeedb")
# print connection
# print("Database connection successfully",conn)
# create a table in database employeedb
cur=conn.cursor()
# execute cursor
# create table users
# cur.execute(
#    """
#    create table if not exists users(
#    id integer primary key autoincrement,
#    name text,
#    email text,
#    mobile integer,
#    address text,
#    country text,
#    state text,
#    city text,
#    salary integer,
#    department text
#    )
#    """
# )


# create table employee
cur.execute(
   
   """
   create table if not exists employee(
   empid integer primary key autoincrement,
   name text,
   email text,
   mobile integer,
   address text,
   age integer,
   country text,
   state text,
   city text,
   salary integer,
   department text
   )
   
   """
)


# create table contact
cur.execute(
   
   """
   create table if not exists contact(
   contactid integer primary key autoincrement,
   name text,
   email text,
   mobile integer,
   messaage text,
   created_date text
   )
   """
)

# create table feedback
cur.execute(
   
   """
   create table if not exists feedback(
   fid integer primary key autoincrement,
   name text,
   email text,
   mobile integer,
   comment int,
   rating text,
   created_at text
   )
   """
)

#insert data in employee 
insertEmployee=[
        (1,"nimesh","nimesh@gmail.com",9998003879,"150 fet ring road",30,"india","gujrat","rajkot",45000,"IT"),
        (2,"rajesh","rajesh@gmail.com",9798003879,"50 fet ring road",21,"india","gujrat","rajkot",35000,"IT"),
        (3,"rupesh","rupesh007@gmail.com",9798003879,"80 fet ring road",20,"india","gujrat","rajkot",25000,"CSE"),
        (4,"nimavat","nimavat@gmail.com",9998003879,"150 fet ring road",30,"india","gujrat","rajkot",45000,"IT"),
        (5,"brijesh","brijesh@gmail.com",9798003879,"50 fet ring road",21,"india","gujrat","rajkot",35000,"IT"),
        (6,"kumar","kumar@gmail.com",9798003879,"80 fet ring road",20,"india","gujrat","rajkot",25000,"CSE"),
        (7,"om","om@gmail.com",9998003859,"150 fet ring road",30,"india","gujrat","rajkot",49000,"IT"),
        (8,"aryan","aryan@gmail.com",9795033879,"50 fet ring road",21,"india","gujrat","rajkot",55000,"IT"),
        (9,"amish","amish007@gmail.com",9793703879,"80 fet ring road",20,"india","gujrat","rajkot",65000,"IT"),
        (10,"lokesh","lokesh@gmail.com",9998403879,"150 fet ring road",30,"india","gujrat","rajkot",85000,"IT"),
        (11,"raj","raj@gmail.com",9798003870,"50 fet ring road",21,"india","gujrat","rajkot",95000,"IT"),
        (12,"manish","manishkumar@gmail.com",9898003879,"80 fet ring road",20,"india","gujrat","rajkot",25000,"CSE")
    ]
# insert data in tables 
cur.executemany(
    """
    insert OR IGNORE into employee values(?,?,?,?,?,?,?,?,?,?,?)
    
    """,insertEmployee)

# display data in tabular layout or dataframe
print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

# fetch all data here
select="select * from employee"
# execute a select query
# cur.execute(select)
# fetch and read all data from sql 
df=pd.read_sql(select,conn)
print("fetch all data successfully :",df)
# fetch data 
# Fetch all data
# data = cur.fetchall()

print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
print(df)
# save query 
conn.commit()
print("employee data successfully added in tables")

# find max salary employee 
print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("max salary get employee :",df["salary"].max())

# find min salary employee 
print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("min salary get employee :",df["salary"].min())

# find sum of salary of all employee 
print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("sum of  salary of all employee :",df["salary"].sum())


# find avg salary from employee 
print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("avg  salary from employee tables  :",df["salary"].mean())

# find a employee name who is getting max  salary from employee 
print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
max_salary_employeename=df.loc[df["salary"].idxmax(), ["name", "salary"]]
print("max salary get employee name from tables :",max_salary_employeename)


# find a employee name who is getting max  salary from employee 
print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
min_salary_employeename=df.loc[df["salary"].idxmin(), ["name", "salary"]]
print("min salary get employee name from tables :",min_salary_employeename)

# create a data visualization in chart
plt.title("salary management app data")
plt.pie(
   df["salary"],
   labels=df["name"],
   colors=["red","green","yellow"],
   autopct="%1.1f%%"
)

plt.show()
# closed connection 
conn.close()