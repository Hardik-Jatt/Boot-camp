import tkinter as tk
import time

class DigitalClock:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Digital Clock")
        self.time_label = tk.Label(self.root, text="", font=("Arial", 40))
        self.time_label.pack()
        self.update_time()
        self.root.mainloop()

    def update_time(self):
        self.time_label.config(text=time.strftime("%H:%M:%S"))
        self.root.after(1000, self.update_time)

if __name__ == "__main__":
    DigitalClock()