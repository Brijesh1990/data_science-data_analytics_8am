# import all library
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import openpyxl
import seaborn as sbn  
import sqlite3 
# connect with database sqlite 
conn=sqlite3.connect("sms-app-db")
# print("database connected successfully")
# create a table 
cur=conn.cursor()
# create a country table schema using cursor 
cur.execute("""
            create table if not exists country(                
                cid integer primary key autoincrement,
                countryname text
            )
            """)
# create a college table schema using cursor 
cur.execute("""
            create table if not exists college(                
                collegeid integer primary key autoincrement,
                collegename text
            )
            """)
# create a department table schema using cursor 
cur.execute("""
            create table if not exists department(                
                depid integer primary key autoincrement,
                depname text
            )
            """)

# create a faculty table schema using cursor 
cur.execute("""
            create table if not exists faculty(                
                facultyid integer primary key autoincrement,
                facultyname text
            )
            """)

# create a students table schema using cursor 
cur.execute("""
            create table if not exists students(                
                stdid integer primary key autoincrement,
                name text,
                age integer,
                address text,
                attendance integer,
                cid integer,
                collegeid integer,
                depid integer,
                facultyid integer,
                foreign key(cid) references country(cid),
                foreign key(collegeid) references college(collegeid), 
                foreign key(depid) references department(depid),
                foreign key(facultyid) references faculty(facultyid)
            )
            """)


# insert a data in tables via sqlite query 
insCountry=[(1,"india"),(2,"usa"),(3,"china")]
cur.executemany("""
                insert or ignore into country values(?,?)
                
                """,insCountry)

insCollege=[(1,"Marwadi univercity"),(2,"Atmiya univercity"),(3,"Govt engg college")]
cur.executemany("""
                insert or ignore into college values(?,?)
                
                """,insCollege)
insDep=[(1,"BDE"),(2,"DA"),(3,"DS")]
cur.executemany("""
                insert or ignore into department values(?,?)
                
                """,insDep)
insFaculty=[(1,"Prof Brijesh"),(2,"Dr aniket"),(3,"prof ruchi")]
cur.executemany("""
                insert or ignore into faculty values(?,?)
                
                """,insFaculty)

insStd=[(1,"om",21,"150 feet  ring road rajkot",1,1,1,1,1),(2,"amish",31,"150 feet  ring road rajkot",0,2,2,2,2),(3,"aryan",22,"50 feet  ring road rajkot",0,1,2,2,3)]
cur.executemany("""
                insert or ignore into students values(?,?,?,?,?,?,?,?,?)
                
                """,insStd)
# print("Data successfully added or inserted")
# print("table created successfully")
# fetch all data via join query
# fetch all data here
print("\n============================================================================================================")
select="select * from students"
df=pd.read_sql(select,conn)
print(df)
# print("fetch all data successfully :",df)
print("\n============================================================================================================")

# fetch all with join data here
print("\n============================================================================================================")
select="select  students.*,countryname,collegename,depname,facultyname from students join country on students.cid=country.cid join college on students.collegeid=college.collegeid join department on students.depid=department.depid join faculty on students.facultyid=faculty.facultyid"
df=pd.read_sql(select,conn)
print(df)
# print("fetch all data successfully :",df)
print("\n============================================================================================================")

# create a Label for attendance 
present = (df["attendance"] == 1).sum()
absent = (df["attendance"] == 0).sum()

# create a data visualization in chart
plt.title("students attendance managements systems")
plt.pie(
   [present, absent],
   labels=["Present", "Absent"],
   colors=["red","green"],
   startangle=90,
   autopct="%1.1f%%"
)

# generate data in excel
excelData=pd.read_sql_query(select,conn)
df=excelData.to_excel("students_data.xlsx", engine="openpyxl", index=False, sheet_name="attendance")

plt.show()
# save query 
conn.commit()
# closed connection 
conn.close()