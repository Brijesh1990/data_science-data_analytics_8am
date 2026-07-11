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
    c) list 
    d) pass 
 
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
# # dictionary examples 
# employees={id:1,"name":"om","age":21,"salary":15500.4568,"department":"IT"}
# print(employees)
# print(type(employees))
# # print only om salary 
# print(employees["salary"])
# print(employees["department"])
# print(employees["age"])
# print(employees["name"])
# print(type(employees["name"]))
# print(type(employees["age"]))
# print(type(employees["salary"]))

# dict() is an inbuilt method defined as a constructor same name of class
# emp=dict({1:"brijesh",2:"om"})
# print(emp)
# print(emp[1])
# print(emp[2])
# note : dict() is defined as same name of class as a constructor 

# what is list ?  
# list is a datatypes of variable that can be stored multiple values is variables 
# list stored data with ["value"] inside of []  
# list is stored mutable data (can be changed or update data in list) 
# list can be add | update | remove data because it is mutable
# list stored multiple data in ["value"] formate
# list can be stored any datatype i.e int | string | float | none | boolean | list , tuple etc 

# examples of list 
# employees=["aryan","om","amish","giriraj",99998003879,True]
# print(employees)
# print(type(employees))
# # print only om from list using slices
# print(employees[1])
# print(employees[0])
# print(employees[0:1])
# print(employees[-1]) 
# print(employees[0:-1])
# print(employees[0:-2])
# print(employees[:-2])
# print(employees[-2])
# print(employees[-3])
# print(employees) 

# add data in list via append
# employees=["aryan","om","amish","giriraj",99998003879,True]
# res=employees.append(["rupesh"])
# res=employees.append("rupesh")
# print(res)
# print(employees)

# update in list
# employees=["aryan","om","amish","giriraj",99998003879,True]
# res=employees.insert(0,"kumar")
# print(res)
# print(employees)

# delete list 
# employees=["aryan","om","amish","giriraj",99998003879,True]
# res=employees.pop()
# print(res)
# print(employees)
# employees=["aryan","om","amish","giriraj",99998003879,True]
# # print(employees[0:1])
# # print(employees[0:-1])
# # print(employees[0:-3])
# del employees
# print(employees)

# list() defined as inbuilt constructor is same name of class 
# employees=list("kumar")
# print(employees.append)
# print(employees)

# employees=list()
# print(employees.append("om"))
# print(employees)

# employees=list()
# # print(employees.append("om"))
# # print(employees)
# del employees
# print(employees)


# what is tuple ? 

# tuple : 

# tuple is a datatypes of variable that can be stored multiple values is variables 
# tuple stored data with () inside of () or with tuple() constructor  
# tuple is stored immutable data (can not be changed or update data in tuple) 
# tuple can not be stored multiple data types values

# how to defined tuple 

# employees=("kumar","om","rajesh")
# print(employees)
# print(type(employees))

# tuple as constructor same name of class 

# employees=tuple("kumar")
# print(employees)
# print(type(employees))

# tuple constructor
# employees=tuple()
# print(employees)
# print(type(employees))

# employees=tuple(("kumar","ravi",999588212, True))
# print(employees)
# print(type(employees))


# remove tuple or delete tuple
# employees=tuple(("kumar","ravi",999588212, True))
# print(employees)
# print(type(employees))
# # delete tuple
# # del employees
# # print(employees)
# print(employees)
  
  
  
# pass : 
# pass is a datatypes of variable 
# pass return nothing 
# pass is immutable (can not be changed)
# pass assigned with pass 

# a=int(input("Enter a values :"))
# b=int(input("Enter b values :"))
# c=a+b 
# print(c)

# def add(a,b):
#    pass
# add(print(10,20))
# in function a and b values return nothing due to pass

# without pass
def add(a):
   return a
add(print(10))