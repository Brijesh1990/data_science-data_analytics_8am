"""

 conditional statements :
  A conditional statements are used to check true or false 
  
  types of conditional statements 
  
    1. if 
    2. if else
    3. if elif
    4. nested if 
    5. switch (python not support)
  
  
  looping statements 
   
   A statements that can be iterate a values again and again there we used loop
   or
   A loop is repeated values again and again 
  
  types of loop 
   1. for 
   2. while 
     
"""


# conditional statements 

# if : if is executed when condition is true  
# syntax 
#  if condition:
#      statements

# examples
# a=2
# b=10
# if a>b:
#     print("a is greater than b") 

# if a>=b:
#     print("a is greater than b") 

# if a>b:
#     print("a is greater than b") 



# if else : if is executed when condition is true if condition is false else is executed  
# syntax 
#  if condition:
#      statements
#    else:
#        statements

# examples
# a=15
# b=10
# if a>b:
#     print("a is greater than b") 
# else:
#     print("a is less than b")

# a=int(input("Enter a values :"))
# b=int(input("Enter b values :"))
# if a>b:
#     print("a is greater than b") 
# else:
#     print("a is less than b")


# nested if : if within an another if i.e called nested if   
# syntax 
#  if condition:
#      if condition:
#         statements
#    else:
#        statements


# a=10
# b=5
# if a>b:
#     if a!=0 and b!=0:
#         print("a is greater than b and both are positive number")

# else:
#     print("a is less than b")



# if elif : if is executed when condition is true elif is check multiple true conditions if conditions is false else is executed

# syntax 

# if condition:
#     statements
# elif condition:
#     statements
# elif condition:
#     statements
# else:
#     statements

# a=30
# b=30
# if a>b:
#     print("a is greater than b")
# elif b>a:
#     print("b is greater than a")
# else:
#     print("a and b both are same") 


# take input from users
# a=int(input("Enter a values :"))
# b=int(input("Enter b values :"))
# if a>b:
#     print("a is greater than b")
# elif b>a:
#     print("b is greater than a")
# else:
#     print("a and b both are same") 



# looping statements : 
# looping statements are executed number of iteration repeat again and again.
# loop is used to executed numbers of iteration again and again 

# syntax
# for i in range():
#     statments

# for i in range(1,10):
#     print(i)

# for i in range(1,100):
#     print(i)

# for i in range(1,100):
#     print(i, end=" ")


# for i in range(1,100):
#     print(i, end =" , ")

# loop with condition
# w.a.p to print 1 to 10 and give only odd numbers 
# for i in range(1,10):
#     if i%2==0:
#         print(i)
# for i in range(1,10):
#     if i%2==1:
#         print(i)

# for i in range(1,10):
#     if i%2!=0:
#         print(i)

# employee={
#     "id":1,
#     "name":"brijesh",
#     "age":35,
#     "department":"IT",
#     "address":"150 feet ring road rajkot"
# }

# for i in employee:
#     print(employee[i])
#     print(employee[i])


# employee={
#     "fname":["nimavat","aryan","om","amish"],
#     "age":[25,21,21,30]
# }
# for i in employee:
    # print(employee["fname"])
    # print(employee["age"])
    # print(employee[i])
    # print(employee[i])
    # print(employee[i][1])
    # print(employee[i][0:1])
    # print(employee[i][0:3])
    # print(employee[i][0:4])
    # print(employee["fname"][0:1])
    
# employee={
#     "fname":["nimavat","aryan","om","amish"],
#     "age":[25,21,21,30]
# }

# iterate only name 
# for i in employee["fname"]:
#     print(i)

# for i in employee["age"]:
#     print(i)
    
    
# employee=["om","amish","aryan","kumar","lokesh","hitesh","astha"]
# for i in employee:
#     print(i)   


# while : while is a loop that can be executed when condition is true 
# syntax 
# while condition:
#     statements
#     increments/decrements

# i=0
# while i<=10:
#     print(i)
#     i=i+1


# i=0
# while i<=10:
#     print(i)
#     i=i+1


# i=0
# while i<=10:
#     if i==5:
#         break
#     print(i)
#     i=i+1
 
 
# i=0
# while i<=10:
#     if i==5 or i==8:
#         i=i+1
#         continue
#     print(i)
#     i=i+1    
 
 
# i=0
# while i<=10:
#     if i  not in(5,8):
#         print(i)
#     i=i+1    

# i=0
# while i<=500:
#     if i  not in(5,8):
#         print(i)
#     i=i+1    


i=0
while i<=10:
    print(i)
    i=i+2
    
  
 
    
     
 

