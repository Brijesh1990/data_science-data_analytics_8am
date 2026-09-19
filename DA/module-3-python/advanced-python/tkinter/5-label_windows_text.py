# import default tkinter 
import tkinter as tk 
# create a simple windows via tkinter 
window=tk.Tk()
# create a windows title 
window.title("simple windows app")
# create a geometry area of windows 
window.geometry("550x500")
# create a label on windows 
label=tk.Label(window, text="Hi i am Aryan", font=("Arial",18), fg="blue")
label.pack(pady=20)
# print windows as output
tk.mainloop()

