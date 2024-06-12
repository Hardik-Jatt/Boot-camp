import tkinter as tk
import getpass

class Login:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Login System")
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.username_label = tk.Label(self.window, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.window, textvariable=self.username)
        self.username_entry.pack()
        self.password_label = tk.Label(self.window, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.window, show="*", textvariable=self.password)
        self.password_entry.pack()
        self.login_button = tk.Button(self.window, text="Login", command=self.check_credentials)
        self.login_button.pack()
        self.window.mainloop()

    def check_credentials(self):
        username = self.username.get()
        password = self.password.get()
        if username == "admin" and password == "password":
            messagebox.showinfo("Success", "Login successful")
        else:
            messagebox.showerror("Error", "Invalid credentials")

Login()