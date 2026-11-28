# banking atm withdrwal systems
# balance defined before the function
# balance can't used inside of function whenever we can not used global keyword
balance=15000
# create a function for each choice 
def chkBalanace():
    global balance
    print("Your bank balance is :",balance)
def depAmount():
    global balance
    amount=int(input("Enter your deposit amount :"))
    if amount<=0:
        print("Can't Deposited This amount something went wrong")
    elif amount>50000:
        print("You Can't Deposited More than 50k in a Day! try again")
    else:
        balance+=amount
        # balance=balance+amount
        print("Your amount deposited Successfully!")
        
def withAmount():
    global balance
    amount=int(input("Enter your Withdrawal amount :"))
    if amount<=0:
        print("Can't Withdrwal This amount something went wrong")
    elif amount>balance:
        print("Insufficient amount for withdrwal check your balance!")
    else:
        balance-=amount
        # balance=balance-amount
        print("Your amount Withdrwal Successfully!")
        
def exAccount():
    print("Thanks for used Our services visit again!")
    
        
    


