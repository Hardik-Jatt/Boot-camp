import tkinter as tk

root = tk.Tk()
var = tk.IntVar()
radiobutton1 = tk.Radiobutton(root, text="Option 1", variable=var, value=1)
radiobutton1.pack()
radiobutton2 = tk.Radiobutton(root, text="Option 2", variable=var, value=2)
radiobutton2.pack()
root.mainloop()