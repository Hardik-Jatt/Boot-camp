import tkinter as tk
from tkinter import messagebox

class Chatbot:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Chatbot")
        self.entry = tk.Entry(self.window, width=40)
        self.entry.pack()
        self.message_label = tk.Label(self.window, text="")
        self.message_label.pack()
        self.send_button = tk.Button(self.window, text="Send", command=self.send_message)
        self.send_button.pack()
        self.window.mainloop()

    def send_message(self):
        message = self.entry.get()
        if message:
            self.entry.delete(0, tk.END)
            self.message_label.config(text=message)
        else:
            messagebox.showerror("Error", "Please enter a message")

Chatbot()