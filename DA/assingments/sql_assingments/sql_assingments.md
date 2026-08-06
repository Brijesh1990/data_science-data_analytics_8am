# sql_assingments  ...

# Working with Database using SQL  Assignment 

# For this assignment, you will finish building the contact management database for MarketCo 

# create a comapny tables with following details 

1. create table company 
(
companyid int AUTO_INCREMENT PRIMARY key,
companyname varchar(100),
state varchar(100),
city varchar(100),
street varchar(100),
zip varchar(100)
   
)


# create a contact us table with following details 

2.  create table contact 
(
contactid int AUTO_INCREMENT PRIMARY key,
companyid int REFERENCES company(companyid),
firstname varchar(255),
lastname varchar(255),
street varchar(100),
state varchar(100),
city varchar(100),
zip varchar(100),
isMain boolean,
email varchar(255),
phone bigint
)


3. 

