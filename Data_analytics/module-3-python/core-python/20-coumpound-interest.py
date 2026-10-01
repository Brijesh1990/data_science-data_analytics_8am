# compound interest
# formula of compound interest
import math
def ci():
    p=int(input("Enter a principle amount :"))
    n=int(input("Enter a Number of years :"))
    r=int(input("Enter a rate of interest :")) 
    # formula of compound interest is .....
    a = p * (1 + r/100)**n
    # calculate compound interest 
    # Calculate compound interest
    # compound_interest = a - p 
    # print("The compound interest is :",compound_interest)
    res=a-p 
    total=res+p 
    final=math.floor(total)
    print("Total you have to paid included with compound interest amount is :",final)
ci()
