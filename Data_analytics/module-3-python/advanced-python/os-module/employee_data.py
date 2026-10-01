with open("om_resume.docx","w") as file:
    if file:
        print("file opened successfully")
    else:
        print("file does not exist")
    
file.close()