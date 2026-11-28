# module reusables 
import logic
# app details 
print("================================")
print("          ATM withdrawal systems")
print("================================")
print("Press 1: for check balance")
print("Press 2: for Deposit amount")
print("Press 3: for check withdrwal amount")
print("Press 4: exit")
# check pin to enter in app
pin=123456
entered_pin=int(input("Enter your Atm Pin : "))
if entered_pin==pin:
    while True:
        choice=int(input("Enter your choice for banking :"))
        if choice==1:
            logic.chkBalanace()
        elif choice==2:
            logic.depAmount()
        elif choice==3:
            logic.withAmount()
        elif choice==4:
            logic.exAccount()
            break
            