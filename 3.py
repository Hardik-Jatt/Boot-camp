import tkinter as tk
import time
import playsound
from PIL import Image, ImageTk

class Pomodoro:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Pomodoro Timer")
        self.label = tk.Label(self.window, text="25:00", font=("Arial", 40))
        self.label.pack()
        self.start_button = tk.Button(self.window, text="Start", command=self.start_timer)
        self.start_button.pack()
        self.break_button = tk.Button(self.window, text="Break", command=self.break_timer)
        self.break_button.pack()
        self.window.mainloop()

    def start_timer(self):
        self.label.config(text="25:00")
        self.window.after(1000, self.decrement_time)

    def break_timer(self):
        playsound.playsound("pomodoro.ogg")

    def decrement_time(self):
        time_str = self.label.cget("text")
        hours, minutes = map(int, time_str.split(":"))
        minutes -= 1
        if minutes < 0:
            minutes = 59
            hours -= 1
        if hours < 0:
            hours = 23
            minutes = 59
        self.label.config(text=f"{hours}:{minutes:02d}")
        self.window.after(1000, self.decrement_time)

Pomodoro()