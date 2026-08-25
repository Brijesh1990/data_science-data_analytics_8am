file=open("looping.txt","r+")
if file:
    print("file open successfully")
else: 
    print("file not opened successfully")

file.close()