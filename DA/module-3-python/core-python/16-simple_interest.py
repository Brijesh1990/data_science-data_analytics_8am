def si():
    p=int(input("Enter a principle amount :"))
    n=int(input("Enter a Number of years :"))
    r=int(input("Enter a rate of interest :"))
    res=p*n*r/100
    print("Simple interest is :",res)
# call a function 
si()