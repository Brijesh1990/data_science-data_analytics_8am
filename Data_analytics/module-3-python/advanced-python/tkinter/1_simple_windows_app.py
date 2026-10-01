import tkinter as tk
# create a windows using tk
window=tk.Tk()
# create a title of windows 
window.title("simple windows app")
# create a geometry of windows 
window.geometry("550x550")
# create a label of windows app
label=tk.Label(window,text="My name is Amish",font=("Arial",19))
label.pack(pady=20)

# print a windows 
tk.mainloop()