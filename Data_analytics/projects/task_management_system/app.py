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

except Exception as e:
    print("something went wrong while connection with database",e)