import tkinter as tk

root = tk.Tk()
menubar = tk.Menu(root)
root.config(menu=menubar)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
root.mainloop()