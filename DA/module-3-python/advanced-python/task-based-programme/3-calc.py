import calcapp
# choice based calculator
print("#############press 1 for additions#############")
print("#############press 2 for substractions#########")
print("#############press 3 for multiplications#######")
print("#############press 4 for divisions#############")
print("#############press 5 for modulas###############")
# reused function while condition is True
while True:
    choice=int(input("Enter your choice :"))
    if choice==1:
        print("Additions of numbers is :",calcapp.add())
    elif choice==2:
        print("Substractions of numbers is :",calcapp.subs())
    elif choice==3:
            print("Multiplications of numbers is :",calcapp.mul())
    elif choice==4:
            print("Divisions of numbers is :",calcapp.dv())
    elif choice==5:
            print("Modulas of numbers is :",calcapp.mod())
    else:
        print("you selected wrong choice")
        break
        