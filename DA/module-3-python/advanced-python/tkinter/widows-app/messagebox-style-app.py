import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk

# ---------------------------------------------------------
# Create Main Window
# ---------------------------------------------------------
window = ttk.Window(themename="superhero")

window.title("Simple Windows App")
window.geometry("550x500")
window.resizable(False, False)


# ---------------------------------------------------------
# Header Section
# ---------------------------------------------------------
header = ttk.Frame(window, bootstyle="primary")
header.pack(fill="x")

title_label = ttk.Label(
    header,
    text="👤  User Information",
    font=("Arial", 24, "bold"),
    bootstyle="inverse-primary"
)
title_label.pack(pady=(25, 5))

subtitle_label = ttk.Label(
    header,
    text="Enter your details below",
    font=("Arial", 11),
    bootstyle="inverse-primary"
)
subtitle_label.pack(pady=(0, 25))


# ---------------------------------------------------------
# Main Card
# ---------------------------------------------------------
card = ttk.Frame(
    window,
    padding=30,
    bootstyle="light"
)
card.pack(padx=40, pady=35, fill="both", expand=True)


# ---------------------------------------------------------
# Label
# ---------------------------------------------------------
label = ttk.Label(
    card,
    text="👋  Enter your Name",
    font=("Arial", 17, "bold"),
    bootstyle="primary"
)
label.pack(pady=(15, 10))


# ---------------------------------------------------------
# Entry Box
# ---------------------------------------------------------
entry_frame = ttk.Frame(card)
entry_frame.pack(fill="x", pady=10)

entry_icon = ttk.Label(
    entry_frame,
    text="👤",
    font=("Arial", 17)
)
entry_icon.pack(side="left", padx=(5, 10))

entry = ttk.Entry(
    entry_frame,
    font=("Arial", 16),
    bootstyle="info"
)
entry.pack(side="left", fill="x", expand=True, ipady=8)


# ---------------------------------------------------------
# Submit Function
# ---------------------------------------------------------
def user_input():
    user_inp = entry.get()

    if user_inp.strip() == "":
        messagebox.showwarning(
            "⚠️ Empty Name",
            "Please enter your name."
        )
        return

    messagebox.showinfo(
        "User Information",
        f"👤 User Name is : {user_inp}"
    )


# ---------------------------------------------------------
# Submit Button
# ---------------------------------------------------------
button = ttk.Button(
    card,
    text="  ✓  Submit  ",
    command=user_input,
    bootstyle="success",
    width=20
)
button.pack(pady=25, ipady=8)


# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------
footer = ttk.Label(
    window,
    text="✨ Simple • Modern • User Friendly",
    font=("Arial", 9),
    bootstyle="secondary"
)
footer.pack(pady=(0, 12))


# ---------------------------------------------------------
# Run Application
# ---------------------------------------------------------
window.mainloop()
