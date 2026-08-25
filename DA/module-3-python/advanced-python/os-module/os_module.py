# file handling removed any file used a os module
import os
path="employee_data.xlsx"
if path:
    res=os.remove("employee_data.xlsx")
    print("file successfully deleted",res)
else:
    print("file does not removed something is wrong")