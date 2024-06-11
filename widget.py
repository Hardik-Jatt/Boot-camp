import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Tkinter Widgets Example")

# Create a label
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# Create an entry field
entry = tk.Entry(root)
entry.pack()

# Create a button
button = tk.Button(root, text="Click Me!")
button.pack()

# Create a checkbutton
checkbutton = tk.Checkbutton(root, text="Check this box")
checkbutton.pack()

# Create a radiobutton
radiobutton = tk.Radiobutton(root, text="Select this option", value=1)
radiobutton.pack()

# Create a scale
scale = tk.Scale(root, from_=0, to=100)
scale.pack()

# Create a scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a text box
text = tk.Text(root, height=10, width=30)
text.pack()

# Create a message box
message = tk.Message(root, text="This is a message box.")
message.pack()

# Create a spinbox
spinbox = tk.Spinbox(root, from_=0, to=10)
spinbox.pack()

# Create a menu
menu = tk.Menu(root)
root.config(menu=menu)

# Create a menu item
menu_item = tk.Menu(menu, tearoff=0)
menu_item.add_command(label="Menu Item 1")
menu_item.add_command(label="Menu Item 2")
menu.add_cascade(label="Menu", menu=menu_item)

# Start the Tkinter event loop
root.mainloop()