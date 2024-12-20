import os
import tkinter as tk
from tkinter import messagebox, Toplevel, Text, Scrollbar, ttk
import pyperclip
from generator import generate_password
from saver import save_to_database, DATA_FILE
import csv


def on_generate_click():
    try:
        length = int(length_entry.get())
        if length < 8:  # Minimum password length check
            messagebox.showwarning("Invalid Length", "Password length should be at least 8 characters.")
            return
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the password length.")
        return

    # Get checkbox and pattern inputs
    use_uppercase = uppercase_var.get()
    use_lowercase = lowercase_var.get()
    use_numbers = numbers_var.get()
    use_specials = specials_var.get()
    complexity = complexity_var.get()
    pattern = pattern_entry.get().lower()  # Convert pattern to lowercase for uniformity

    # Generate the password
    password = generate_password(
        length=length,
        use_uppercase=use_uppercase,
        use_lowercase=use_lowercase,
        use_numbers=use_numbers,
        use_specials=use_specials,
        pattern=pattern,
        complexity=complexity
    )

    # Display the generated password
    password_label.config(text=password)


def on_copy_click():
    # Copy the password to clipboard
    password = password_label.cget("text")
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password has been copied to the clipboard!")
        # Save to the database
        save_to_database(password)
    else:
        messagebox.showwarning("No Password", "Generate a password first!")


# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.resizable(False, False)

# Create and place the labels, entries, and buttons
tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Pattern (e.g., 'ulsn'):").grid(row=1, column=0, padx=10, pady=10)
pattern_entry = tk.Entry(root)
pattern_entry.grid(row=1, column=1, padx=10, pady=10)

strength_label = tk.Label(root, text="Password Strength: ", font=("Arial", 12, "bold"))


def view_saved_passwords():
    """Display all saved passwords in a new window."""
    if not os.path.isfile(DATA_FILE):
        messagebox.showinfo("No Data", "No passwords have been saved yet!")
        return

    # Create a new window
    view_window = Toplevel()
    view_window.title("Saved Passwords")
    view_window.geometry("500x300")
    view_window.resizable(False, False)

    # Style the Treeview widget
    style = ttk.Style()
    style.configure("Treeview", font=("Segoe UI", 11), rowheight=25)
    style.configure("Treeview.Heading", font=("Segoe UI", 12, "bold"))
    style.map("Treeview", background=[("selected", "#347083")])  # Highlight selection color

    # Create a Treeview for displaying passwords
    tree = ttk.Treeview(view_window, columns=("Password", "Copied On"), show="headings", height=10)
    tree.heading("Password", text="Password")
    tree.heading("Copied On", text="Copied On")
    tree.column("Password", anchor="center", width=200)
    tree.column("Copied On", anchor="center", width=250)

    # Colors
    tree.tag_configure("evenrow", background="#F0F0F0")
    tree.tag_configure("oddrow", background="#FFFFFF")

    # Add a scrollable text widget
    scrollbar = Scrollbar(view_window, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    tree.pack(expand=True, fill="both")

    text_widget = Text(view_window, wrap="none", yscrollcommand=scrollbar.set)
    text_widget.pack(expand=True, fill="both")
    scrollbar.config(command=text_widget.yview)

    # Read the saved passwords
    with open(DATA_FILE, mode="r") as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip the header row
        for index, row in enumerate(reader):
            tag = "evenrow" if index % 2 == 0 else "oddrow"
            tree.insert("", "end", values=(row[0], row[1]), tags=(tag,))

    # Optional: Add a button to close the window
    close_button = ttk.Button(view_window, text="Close", command=view_window.destroy)
    close_button.pack(pady=10)


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

# View saved passwords button
view_button = tk.Button(root, text="View Saved Passwords", command=view_saved_passwords)
view_button.grid(row=10, column=0, columnspan=2, padx=10, pady=10)
view_button.config(bg="lightblue")
# Start the  main loop
root.mainloop()
