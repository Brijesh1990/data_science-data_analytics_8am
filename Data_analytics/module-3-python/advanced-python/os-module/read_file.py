with open("employee_data.xlsx","w") as file:
    if file:
        print("file opened successfully")
    else:
        print("file does not exist")
    
file.close()