# sql_assesements  ...

1. create database superstore_dataset_final; 
2. What is the functional difference between SELECT * and specifying column
names, and when is each preferred  ?

**Answer**

1. select * is used to select all the data rows * meanse all the data 
   
```
create table employee
(
empid int AUTO_INCREMENT primary key,
name varchar(255),
age int,
phone bigint,
salary int, 
department varchar(255)

)

```

2. select * from employee 

3. select columnname is used to select particular columns of table 

  ```
  select empid,name,phone, salary from employee
  
  ```

4. Which keyword renames a column in the output, and does this alias change
the actual table structure in the database  ?

**answer**
1. yes we can rename the column name using alter and there is no any effects on table structures after rename or change column name is table 

```
alter table employee change name employee_name varchar(255)

```

5. Why does wrapping a numeric value in quotes (e.g., '5000') in a WHERE clause
create a data type conflict in SQL ?

**answer**

1.wrapping a numeric values depend on table column data types if its is varchar so need to wrapp in '' if it is int not need to warapp in ''  


```
select * from employee where empid='1'
```


6. Contrast the results of ORDER BY Profit DESC versus ASC when the goal is to
identify the top 10 most profitable orders ?


7. What is the T-SQL equivalent of the LIMIT clause in MS SQL Server, and why
does syntax vary across SQL engines  ?

**answer**

1. limit is used to select data on range based from tables 
2. its syntax vary in different - 2 databases 
3. in mysql its is used like ...

 ```
 select * from employee where empid limit 0,2;
 ```
   
8. Explain the logical execution order of a query containing SELECT, WHERE, ORDER
BY, and LIMIT clauses. 


**answer**

 1. select 
     
 2. where

 3. order by 
 
 4. limit 

 ```
  select * from employee
  or
  select * from employee where empid='1'
  or
  select * from employee  order by empid desc
  or
  select * from employee  where empid limit 0,2
 
 ```
