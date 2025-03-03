import tkinter as tk
import pyperclip

# Caesar Cipher Functions
def caesar_cipher(text, shift, decrypt=False):
    if decrypt:
        shift = -shift
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

# Encrypt & Decrypt Handlers
def encrypt():
    result_var.set(caesar_cipher(entry.get(), int(shift_entry.get())))

def decrypt():
    result_var.set(caesar_cipher(entry.get(), int(shift_entry.get()), decrypt=True))

def paste_text():
    entry.delete(0, tk.END)
    entry.insert(0, pyperclip.paste())

def copy_result():
    pyperclip.copy(result_var.get())

def on_entry_click(event):
    if entry.get() == "Enter text here...":
        entry.delete(0, tk.END)
        entry.config(fg="black")

def on_focus_out(event):
    if entry.get() == "":
        entry.insert(0, "Enter text here...")
        entry.config(fg="gray")

# GUI Setup
root = tk.Tk()
root.title("Caesar Cipher")
root.geometry("620x200")
root.configure(bg="#F5F5F5")  # Light gray background

# Title Label
tk.Label(root, text="Text Encryptor", font=("Arial", 18, "bold"), fg="black", bg="#F5F5F5").grid(row=0, column=1, columnspan=2, pady=5)

# Input Field
tk.Label(root, text="Enter Text:", font=("Arial", 12), fg="black", bg="#F5F5F5").grid(row=1, column=0, padx=5, sticky="e")
entry = tk.Entry(root, width=50, font=("Arial", 12), fg="gray")
entry.grid(row=1, column=1, padx=5, pady=5)
entry.insert(0, "Enter text here...")
entry.bind("<FocusIn>", on_entry_click)
entry.bind("<FocusOut>", on_focus_out)
tk.Button(root, text="Paste", command=paste_text, bg="lightblue", font=("Arial", 10)).grid(row=1, column=2, padx=5)

# Shift Value
tk.Label(root, text="Shift Value:", font=("Arial", 12), fg="black", bg="#F5F5F5").grid(row=2, column=0, padx=5, sticky="e")
shift_entry = tk.Entry(root, width=5, font=("Arial", 12))
shift_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
shift_entry.insert(0, "3")

# Encrypt & Decrypt Buttons
tk.Button(root, text="Encrypt", command=encrypt, bg="green", fg="white", font=("Arial", 12)).grid(row=3, column=1, sticky="w", padx=5)
tk.Button(root, text="Decrypt", command=decrypt, bg="red", fg="white", font=("Arial", 12)).grid(row=3, column=1, sticky="e", padx=5)

# Result Field
tk.Label(root, text="Result:", font=("Arial", 12), fg="black", bg="#F5F5F5").grid(row=4, column=0, padx=5, sticky="e")
result_var = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result_var, width=50, font=("Arial", 12), state='readonly')
result_entry.grid(row=4, column=1, padx=5, pady=5)
tk.Button(root, text="Copy", command=copy_result, bg="lightblue", font=("Arial", 10)).grid(row=4, column=2, padx=5)

root.mainloop()
