import tkinter as tk

root = tk.Tk()
listbox = tk.Listbox(root)
listbox.insert(1, "Item 1")
listbox.insert(2, "Item 2")
listbox.pack()
root.mainloop()