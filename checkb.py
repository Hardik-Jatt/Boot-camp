import tkinter as tk

root = tk.Tk()
var = tk.IntVar()
checkbutton = tk.Checkbutton(root, text="Check me", variable=var)
checkbutton.pack()
root.mainloop()