import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 
import openpyxl
import mysql.connector
from mysql.connector import Error

# connection 
try:
    conn=mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root", 
        password="admin",
        database="product_db_app"
    )
    if conn.is_connected():
        print('connection successfully stablished')
    
    # create product inventory app
    print("===========================================================")
    print("Product inventory App")
    print("===========================================================")
    print("1. Add product Category")
    print("2. Add products")
    print("3. display all products")
    print("4. Search products")
    print("5. Update products details")
    print("6. Delete products Data")
    print("7. Export all products data in Excel")
    print("8. Display all products in pie chart which status in active")
    print("9. Exit")
    
    # add category
    def add_category():
        # create a tables of category
        cur=conn.cursor()
        cur.execute("""
                    create table if not exists tbl_category(
                        catid int auto_increment primary key, 
                        catname varchar(255),
                        added_date varchar(255)
                    )                  
                    """)
        conn.commit()
        print('table created successfully')
        # insert category in tables
        catname=input("Enter your categoryName :")
        added_date=input("Enter added date :")
        insertCategory=(catname,added_date)
        cur.execute("""
                        insert  into tbl_category(catname,added_date) values(%s,%s)
                        """,insertCategory)
        conn.commit()
        print("category added successfully")
        
    # add products
    def add_products():
        productname=input("Enter your categoryName :")
        catid=int(input("Enter category Id :"))
        price=int(input("Enter product Price :"))
        qty=int(input("Enter product qty :"))
        description=input("Enter product descriptions :")
        added_date=input("Enter added date :")
    
    # enter choices 
    while True:
        # enter choices 
        choice=int(input("Enter your choice :"))
        if choice==1:
            add_category()
        elif choice==2:
            add_products()
        elif choice==9:
          break  
            
except Error as e:
    print('something went wrong',e)