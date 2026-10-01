# choice based calculator
print("#############press 1 for additions#############")
print("#############press 2 for substractions#########")
print("#############press 3 for multiplications#######")
print("#############press 4 for divisions#############")
print("#############press 5 for modulas###############")

# create a function for all calculations
def add():
    a=int(input("Enter a values :"))
    b=int(input("Enter b values :"))
    return a+b
def subs():
    a=int(input("Enter a values :"))
    b=int(input("Enter b values :"))
    return a-b
def mul():
    a=int(input("Enter a values :"))
    b=int(input("Enter b values :"))
    return a*b
def dv():
    a=int(input("Enter a values :"))
    b=int(input("Enter b values :"))
    return a/b
def mod():
    a=int(input("Enter a values :"))
    b=int(input("Enter b values :"))
    return a%b

# reused function while condition is True

while True:
    choice=int(input("Enter your choice :"))
    if choice==1:
        print("Additions of numbers is :",add())
    elif choice==2:
        print("Substractions of numbers is :",subs())
    elif choice==3:
            print("Multiplications of numbers is :",mul())
    elif choice==4:
            print("Divisions of numbers is :",dv())
    elif choice==5:
            print("Modulas of numbers is :",mod())
    else:
        print("you selected wrong choice")
        break
        