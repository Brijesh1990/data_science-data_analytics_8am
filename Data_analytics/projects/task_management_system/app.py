import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as snb 
import numpy as np 
import openpyxl
import mysql.connector
from mysql.connector import Error
# create a database connection 
try:
    conn=mysql.connector.connect(
        host='127.0.0.1',
        port=3306, 
        user="root",
        password="admin",
        database="tsk_app_db"
    )
    
    if conn.is_connected():
        print("database connected successfully")
    else:
        print("something went wrong")
        
    # create a tables in database 
    cur=conn.cursor()
    # create table assign to 
    cur.execute("""
                create table if not exists assignto(
                    empid int primary key auto_increment,
                    empname varchar(255),
                    age int,
                    address text,
                    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
                """)
    # create table assign to 
    cur.execute("""
                create table if not exists task(
                    taskid int primary key auto_increment,
                    title varchar(255),
                    empid int,
                    foreign key(empid) references assignto(empid),
                    descriptions text,
                    status varchar(255),
                    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
                """)
    
    print('tables created successfully')
    
    print("\n=====select 1 for add employee details======")
    print("\n=====select 2 for add task======")
    print("\n=====select 3 for display all task======")
    print("\n=====select 4 exit task =====")
    # create a task on choice based 
    while True:
        choice=int(input("Enter your choice :"))
        if choice==1:
            empname=input("Enter employee Name :")
            age=int(input("Enter employee age :"))
            address=input("Enter employee address :")
            # add employee 
            cur=conn.cursor()
            data=(empname,age,address)
            cur.execute("""
                        insert into assignto(empname,age,address) values(%s,%s,%s)
                        
                        """,data)
            print('employee added successfully')
            conn.commit()
        elif choice==2:
            title=input("Enter task title Name :")
            empid=int(input("Enter employee id for assign to task :"))
            descriptions=input("Enter task descriptions :")
            status=input("Enter task status :")
            # add task 
            cur=conn.cursor()
            data=(title,empid,descriptions,status)
            cur.execute("""
                    insert into task(title,empid,descriptions,status) values(%s,%s,%s,%s)
                    """,data)
            print('task added successfully')
            conn.commit()
            
        

except Exception as e:
    print("something went wrong while connection with database",e)