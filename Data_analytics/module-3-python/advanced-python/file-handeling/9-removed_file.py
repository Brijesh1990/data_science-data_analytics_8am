# file handling removed any file used a os module
import os
path="data.txt"
if path:
    res=os.remove("data.txt")
    print("file successfully deleted",res)
else:
    print("file does not removed something is wrong")