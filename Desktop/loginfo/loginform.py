import tkinter as tk
from tkinter import messagebox

# Hardcoded credentials for demo purposes
VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Form")
        self.root.geometry("300x200")
        self.root.resizable(False, False)

        # Username
        tk.Label(root, text="Username:").pack(pady=5)
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        # Password
        tk.Label(root, text="Password:").pack(pady=5)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        # Buttons
        tk.Button(root, text="Login", command=self.login).pack(pady=10)
        tk.Button(root, text="Clear", command=self.clear_fields).pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showwarning("Input Error", "Please enter both fields.")
        elif username == VALID_USERNAME and password == VALID_PASSWORD:
            messagebox.showinfo("Success", "Login Successful!")
        else:
            messagebox.showerror("Error", "Invalid credentials.")

    def clear_fields(self):
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
