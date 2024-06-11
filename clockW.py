import tkinter as tk
import math
import time

class AnalogClock:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Analog Clock")
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg='white')
        self.canvas.pack()
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        self.canvas.delete("all")
        origin_x = 200
        origin_y = 200
        self.canvas.create_oval(50, 50, 350, 350, width=2)
        for i in range(1, 13):
            x = origin_x + 150 * math.sin(math.radians(i * 30))
            y = origin_y - 150 * math.cos(math.radians(i * 30))
            self.canvas.create_text(x, y, text=str(i), font=("Arial", 12))
        self.draw_hands(origin_x, origin_y)
        self.root.after(1000, self.update_clock)

    def draw_hands(self, origin_x, origin_y):
        now = time.localtime()
        hour = now.tm_hour % 12 + now.tm_min / 60
        minute = now.tm_min
        second = now.tm_sec
        hour_angle = math.radians((hour * 30) - 90)
        minute_angle = math.radians((minute * 6) - 90)
        second_angle = math.radians((second * 6) - 90)
        hour_x = origin_x + 75 * math.sin(hour_angle)
        hour_y = origin_y - 75 * math.cos(hour_angle)
        minute_x = origin_x + 100 * math.sin(minute_angle)
        minute_y = origin_y - 100 * math.cos(minute_angle)
        second_x = origin_x + 120 * math.sin(second_angle)
        second_y = origin_y - 120 * math.cos(second_angle)
        self.canvas.create_line(origin_x, origin_y, hour_x, hour_y, width=3)
        self.canvas.create_line(origin_x, origin_y, minute_x, minute_y, width=2)
        self.canvas.create_line(origin_x, origin_y, second_x, second_y, width=1, fill='red')

if __name__ == "__main__":
    AnalogClock()