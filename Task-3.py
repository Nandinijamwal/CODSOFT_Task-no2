import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    # characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # random password of the specified length
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def display_password():
    try:
        length = int(entry.get())
        if length <= 0:
            raise ValueError
        password = generate_password(length)
        messagebox.showinfo("Generated Password", f"Your Password: {password}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive number.")

#main window
root = tk.Tk()
root.title("Password Generator")

#label, entry, and button widgets
tk.Label(root, text="Enter the desired length of the password:").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)
tk.Button(root, text="Generate Password", command=display_password).pack(pady=10)

#event loop
root.mainloop()
