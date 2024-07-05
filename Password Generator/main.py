import random
import string
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password= "".join(random.choice(characters) for i in range(var.get()))

    output.config(text = password)
    output.config(text = password, font=("Ubuntu", 20), justify= 'center')

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(output.cget("text"))

root = ThemedTk(theme="Equilux")
root.title("Password Generator")
root.geometry("400x200")

var = tk.IntVar()
var.set(0)

dropdown = ttk.Combobox(root, textvariable= var, values=[8,9,10,11,12,13,14,15,16,17,18,19,20])
dropdown.pack(pady=20)

generate_button = ttk.Button(root, text="Generate", command=generate_password)
generate_button.pack()

copy_button= ttk.Button(root, text="Copy", command= copy_to_clipboard)
copy_button.pack(pady=5)

output = ttk.Label(root)
output.pack(pady=15)

root.mainloop()