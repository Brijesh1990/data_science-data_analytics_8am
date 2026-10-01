with open("module_python.txt","a+") as file:
    txt="\n Module in python is a peace of file that can save with .py"
    print(file.write(txt))
file.close()