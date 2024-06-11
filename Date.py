import tkinter as tk
import calendar

class Calendar:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calendar")
        self.year = tk.StringVar()
        self.year.set("2024")
        self.year_label = tk.Label(self.root, text="Year:")
        self.year_label.pack()
        self.year_entry = tk.Entry(self.root, textvariable=self.year)
        self.year_entry.pack()
        self.show_button = tk.Button(self.root, text="Show Calendar", command=self.show_calendar)
        self.show_button.pack()
        self.root.mainloop()

    def show_calendar(self):
        year = int(self.year.get())
        cal = calendar.monthcalendar(year, 1)
        for row in cal:
            for day in row:
                if day:
                    print(f"{day:02}", end=" ")
            print()

if __name__ == "__main__":
    Calendar()