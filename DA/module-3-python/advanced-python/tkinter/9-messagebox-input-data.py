# import default tkinter 
import tkinter as tk 
# pass a message in popup box 
import tkinter.messagebox as message 
# create a simple windows via tkinter 
window=tk.Tk()
# create a windows title 
window.title("simple windows app")
# create a geometry area of windows 
window.geometry("550x500")
# create a function print name dynamic
def user_input():
    user_inp=entry.get()
    # messagebox in popup
    return message.showinfo("User information is :",f'User Name is :{user_inp}',)
# create a label on windows 
label=tk.Label(window, text="Enter your Name : ", font=("Arial",18), fg="blue")
label.pack(pady=20)
# create a widget for user input 
entry=tk.Entry(window,text="Enter your name :",font=("Arial",18))
entry.pack(pady=10)
# create a button widget
button=tk.Button(window, text="Submit" , font=("Arial",20), fg="blue", command=user_input)
button.pack(pady=20)
# print windows as output
tk.mainloop()
