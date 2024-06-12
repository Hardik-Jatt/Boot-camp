import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Scientific Calculator")
        self.entry = tk.Entry(self.window, width=20)
        self.entry.pack()
        self.button_frame = tk.Frame(self.window)
        self.button_frame.pack()
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]
        row_val = 0
        col_val = 0
        for button in buttons:
            tk.Button(self.button_frame, text=button, width=5, command=lambda button=button: self.click(button)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
        self.window.mainloop()

    def click(self, button):
        if button == "=":
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        else:
            self.entry.insert(tk.END, button)

ScientificCalculator()