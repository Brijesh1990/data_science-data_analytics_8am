""" 
what is variables data types ? 
 A data types are which type of values stored in variable i.e called datatypes 
 A data types are two types ...
 
 1) primitive data types
    a) integer 
    b) string 
    c) float 
    d) boolean 
    e) null 
    f) undefined 
    
 2) non primitive datatypes 
 
    a) dictionary
    b) tuple
    c) pass 
    d) list 
 
for check any data type of variable we used type() inbuilt method
 
"""

# integer 

# a=10
# b=51221635223
# c=106555121
# print(a)
# print(type(a))


# float or decimal 
# a=10.653321
# b=14545.32
# c=1454.235656565
# print(c)
# print(type(c))

# string :
# string is a set of character enclosed within '' or "" or """""" i.e called string
# string is a set of characters 

# name="brijesh"
# name1="amish kumar"
# name2="""kumar"""
# name3='aryan'
# print(name2)
# print(type(name2))

# boolean 
# boolean stored tue and false i.e called boolean 

# a=True 
# b=False 
# print(a)
# print(type(a))

# a=10
# b=20
# # print(a!=b)
# # print(type(a!=b))
# # c=a+b
# # print(type(c))
# print(a==b)
# print(type(a==b))


# null or None
# a=None
# print(a)
# print(type(a))

# undefined 
# not defined any values inside of variables 
# a 
# print(a)
# print(type(a))


# what is dictionary ?  
# dictionary is  a datatypes of variables that can be stored multiple values is variables 
# dictionary stored data with {key:values} inside of {} 
# dictionary is stored mutable data (can be changed) 
# dictionary can be add | update | remove data because it is mutable
# dictionary stored multiple data in for of {key:values}
# dictionary can be stored any datatype i.e int | string | float | none | boolean | list , tuple etc 

employees={id:1,"name":"om","age":21,"salary":15500.4568,"department":"IT"}
print(employees)
print(type(employees))
# print only om salary 
print(employees["salary"])
print(employees["department"])
print(employees["age"])
print(employees["name"])
print(type(employees["name"]))
print(type(employees["age"]))
print(type(employees["salary"]))