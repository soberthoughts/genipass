import tkinter as tk
from tkinter import messagebox
import pyperclip
from generator import generate_password


def on_generate_click():
    try:
        length = int(length_entry.get())
        if length < 8:  # Minimum password length check
            messagebox.showwarning("Invalid Length", "Password length should be at least 8 characters.")
            return
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the password length.")
        return

    use_uppercase = uppercase_var.get()
    use_lowercase = lowercase_var.get()
    use_numbers = numbers_var.get()
    use_specials = specials_var.get()
    complexity = complexity_var.get()
    pattern = pattern_entry.get()

    # Generate the password using the generator function
    password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_specials, pattern, complexity)

    # Display the generated password
    password_label.config(text=password)


def on_copy_click():
    # Copy the password to clipboard
    password = password_label.cget("text")
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password has been copied to the clipboard!")
    else:
        messagebox.showwarning("No Password", "Generate a password first!")


# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place the labels, entries, and buttons
tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Pattern (e.g., 'ulsn'):").grid(row=1, column=0, padx=10, pady=10)
pattern_entry = tk.Entry(root)
pattern_entry.grid(row=1, column=1, padx=10, pady=10)

# Checkbox options for character types
uppercase_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Uppercase", variable=uppercase_var).grid(row=2, column=0, padx=10, pady=5,
                                                                            columnspan=2)
lowercase_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Lowercase", variable=lowercase_var).grid(row=3, column=0, padx=10, pady=5,
                                                                            columnspan=2)
numbers_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).grid(row=4, column=0, padx=10, pady=5, columnspan=2)
specials_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Special Characters", variable=specials_var).grid(row=5, column=0, padx=10, pady=5,
                                                                                    columnspan=2)

# Complexity level dropdown
tk.Label(root, text="Password Complexity:").grid(row=6, column=0, padx=10, pady=10)
complexity_var = tk.StringVar(value='medium')
tk.OptionMenu(root, complexity_var, 'low', 'medium', 'high').grid(row=6, column=1, padx=10, pady=10)

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=on_generate_click)
generate_button.grid(row=7, column=0, padx=10, pady=10, columnspan=2)

# Password display label
password_label = tk.Label(root, text="Your generated password will appear here", font=('Helvetica', 12, 'bold'))
password_label.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

# Copy button
copy_button = tk.Button(root, text="Copy to Clipboard", command=on_copy_click)
copy_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

# Start the  main loop
root.mainloop()
