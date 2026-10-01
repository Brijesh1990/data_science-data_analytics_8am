with open("file_handling.txt","w") as file:
    txt="\n with is method to open file and create an alias of file"
    txt1="\n with is used in file handling to create open any file"
    print(file.write(txt))
    print(file.write(txt1))
file.close()