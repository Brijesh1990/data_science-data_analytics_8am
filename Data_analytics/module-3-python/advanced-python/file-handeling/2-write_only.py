file=open("data.txt","w")
if file:
    print("file open successfully")
else: 
    print("file not opened successfully")

file.close()