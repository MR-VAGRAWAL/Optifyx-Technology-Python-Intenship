import random
import string
import tkinter as tk
from tkinter import messagebox
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Invalid Input", "Password length should be a positive integer.")
            return
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer for password length.")
        return
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if uppercase_var.get() else ''
    digit_chars = string.digits if digits_var.get() else ''
    symbol_chars = string.punctuation if symbols_var.get() else ''
    all_chars = lowercase_chars + uppercase_chars + digit_chars + symbol_chars
    if not all_chars:
        messagebox.showerror("Error", "Select at least one character set.")
        return
    password = ''.join(random.choice(all_chars) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard")
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("450x350")
root.configure(bg="#E8F0F2")
title_label = tk.Label(root, text="Random Password Generator", font=("Arial", 17, "bold"), bg="#E8F0F2")
title_label.pack(pady=10)
tk.Label(root, text="Password Length:", font=("Arial", 12), bg="#E8F0F2").pack(pady=5)
length_entry = tk.Entry(root, font=("Arial", 12), width=5)
length_entry.pack(pady=5)
uppercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var, bg="#E8F0F2").pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Digits", variable=digits_var, bg="#E8F0F2").pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var, bg="#E8F0F2").pack(anchor='w', padx=20)
generate_button = tk.Button(root, text="Generate", command=generate_password, font=("Arial", 12), bg="#4CAF50", fg="white")
generate_button.pack(pady=10)
password_entry = tk.Entry(root, width=30, font=("Arial", 12))
password_entry.pack(pady=5)
copy_button = tk.Button(root, text="Copy", command=copy_password, font=("Arial", 12), bg="#2196F3", fg="white")
copy_button.pack(pady=5)
root.mainloop()
