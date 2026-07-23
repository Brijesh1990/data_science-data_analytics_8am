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
a=int(input("Enter a values :"))
b=int(input("Enter b values :"))
if a>b:
    print("a is greater than b")
elif b>a:
    print("b is greater than a")
else:
    print("a and b both are same") 

