# import all library
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
import openpyxl
import sqlite3
# connect database 
conn=sqlite3.connect("students_management_db")
# print("database connected successfully",conn)
# create cursor
cur=conn.cursor()
# create table country
cur.execute(
    """ 
    create table if not exists country(
        cid integer primary key autoincrement,
        cname text
    )
    """
)
# create table state
cur.execute(
    """ 
    create table if not exists state(
        sid integer primary key autoincrement,
        sname text
    )
    """
)

# create table city
cur.execute(
    """ 
    create table if not exists city(
        ctid integer primary key autoincrement,
        ctname text
    )
    """
)

# create table department
cur.execute(
    """ 
    create table if not exists department(
        depid integer primary key autoincrement,
        depname text
    )
    """
)

# create table college
cur.execute(
    """ 
    create table if not exists college(
        collegeid integer primary key autoincrement,
        collegename text
    )
    """
)

# create table faculty
cur.execute(
    """ 
    create table if not exists faculty(
        fid integer primary key autoincrement,
        fname text,
        femail text,
        fmobile integer,
        faddress text
    )
    """
)


# create table students
cur.execute(
    """ 
    create table if not exists students(
        studentid integer primary key autoincrement,
        name text,
        email text,
        mobile integer,
        address text,
        cid integer,
        sid integer,
        ctid integer,
        depid integer,
        collegeid integer,
        fid integer,
        attid integer,
        foreign key(cid) references country(cid),
        foreign key(sid) references state(sid), 
        foreign key(ctid) references city(ctid),
        foreign key(depid) references department(depid),
        foreign key(collegeid) references college(collegeid),
        foreign key(fid) references faculty(fid),
        foreign key(attid) references attendance(attid)
        
    )
    """
)
# create to insert data country
insCountry=[
    (1,'india'),
    (2,'usa'),
    (3,'china')
]
cur.executemany(
    """ 
    insert or ignore into country values(?,?)
    """,insCountry
)
# create to insert data state
insState=[
    (1,'gujrat'),
    (2,'california'),
    (3,'sanghai')
]
cur.executemany(
    """ 
    insert or ignore into state values(?,?)
    """,insState
)
# create to insert data city
insCity=[
    (1,'rajkot'),
    (2,'ahemdabad'),
    (3,'los angeles'),
    (4,'Bezing')
]
cur.executemany(
    """ 
    insert or ignore into city values(?,?)
    """,insCity
)
# create to insert data departement
insDep=[
    (1,'IT'),
    (2,'CSE'),
    (3,'Data analysis'),
    (4,'Data science')
]
cur.executemany(
    """ 
    insert or ignore into department values(?,?)
    """,insDep
)

# create to insert data college
insColl=[
    (1,'Marawadi univercity'),
    (2,'Atmiya Univercity'),
    (3,'Darashn univercity'),
    (4,'Govt Engg college')
]
cur.executemany(
    """ 
    insert or ignore into department values(?,?)
    """,insColl
)

# create to insert data faculty
insFac=[
    (1,'Dr. Dinesh Patel','dinesh008@gmail.com',653695489,'150 feet ring road rajkot'),
    (2,'Dr. Maru agrawal','maru07@gmail.com',753995489,'50 feet ring california'),
    (3,'Prof. rupesh chandela','rupesh008@gmail.com',993695489,'150 feet ring road ahemdabad'),
    (4,'Prof minali shah','minal098@gmail.com',953695789,'50 feet ring road surat')
]
cur.executemany(
    """ 
    insert or ignore into faculty values(?,?,?,?,?)
    """,insFac
)


# create to insert data students
insStd=[
(1,'Om','om008@gmail.com',9853695489,'150 feet ring road rajkot',1,1,1,1,1,1,1),
(2,'Amish','amish07@gmail.com',9653995489,'50 feet ring california',1,2,3,2,1,1,1),
(3,'Aryan','arayan008@gmail.com',7853695489,'150 feet ring road ahemdabad',1,2,3,2,1,1,1),
(4,'Giriraj','girir098@gmail.com',9983695789,'50 feet ring road rajkot',1,2,3,2,1,1,1)
]
cur.executemany(
    """ 
    insert or ignore into students values(?,?,?,?,?,?,?,?,?,?,?,?)
    """,insStd
)


# save a query 
conn.commit()
# print("table created successfully")
print("Data inserted successfully")
# closed connection  
conn.close()