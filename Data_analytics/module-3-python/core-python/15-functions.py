"""

what is function in python ?
A function is a block of code that can be used to completed any task i.e called function 
A function can be declared by def keyword 
A function can be reused 
A function can be return a values 
A function should be call

syntax of function

def functioname():
    statements
call function    


# types of function 
# 1. user defined function
# 2. pre defined function  
    
# how to call function 
# there are two way to call any function 
# 1) function call by values 
# 2) function call by reference 

    
""" 
# w.a.p to print your name using function 

# def name():
#     nm="hi Brijesh"
#     print(nm)
# name() #call function

# w.a.p to print your name via function return 

# def name():
#     nm="hi Brijesh"
#     return nm #function is terminated here in body
# print(name()) #call function

#w.a.p to call any function via its parameter or argument to call by values
# def display(fnm):
#     firstName="My firstname is :"+fnm
#     print(firstName)     
# display("Om")

# def display(fnm,lnm,age):
#     firstName="My firstname is :"+fnm+"\n"
#     lastName="My lastname is :"+lnm+"\n"
#     Age="My age is :",age
#     print(firstName,lastName,Age)     
# display("Om","Makwana",21)


# w.a.p of user defined function 

# def om():
#     fnm="my firstname is : OM Makwana"+"\n"
#     age="my age is 21 years old"
#     print(fnm,age)
# om()


# w.a.p to print pre defined function 
# which is defined by systems i.e called pre defined function
# a=10
# print(type(a))
# name="brijesh"
# res=name.upper()
# print(res)

# name="brijesh"
# res=name.capitalize()
# print(res)


# w.a.p to call any function call by value
# def add(a,b):
#     c=a+b 
#     return c
# print(add(10,20)) # function call by values

# w.a.p to print any function call by reference 
# def Address(fnm,lnm,address):
#     firstName="My firstName is :"+fnm+"\n"
#     lastName="My lastName is :"+lnm+"\n"
#     address="My address is :"+address+"\n"
#     print(firstName,lastName,address)
# Address("Brijesh","Pandey","150 feet ring road rajkot-360005")


# function scope : call any function inside of function block i.e called local scope of functions


# function scope : call any function inside of function block or outside of function block  i.e called global scope of functions

# local scope 
# def nm():
#     name="Brijesh"
#     print(name)
# nm()

# global scope
# name="brijesh"
# def nm():
#     print(name)
# nm()


# function reused one module to another module 
# function should be reused one module to another module 


