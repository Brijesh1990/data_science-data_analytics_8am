# calculate electricity per units charge
units=int(input("Enter your unit that you are used : "))
def electric():
    if units<=100:
        res=(units*5)
        return res
    elif units >100:
        res=(100*5)+(units-100)*7
        return res
    else:
        res=(100*5)+(units-100)*7+(units-200)*10
        return res
    
    
            
    