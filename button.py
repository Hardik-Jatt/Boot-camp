import tkinter as tk

root = tk.Tk()
def button_clicked():
    print("Button clicked")

button = tk.Button(root, text="Click me", command=button_clicked)
button.pack()
root.mainloop()