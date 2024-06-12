import tkinter as tk

class CompoundInterest:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Compound Interest Calculator")
        self.principal = tk.DoubleVar()
        self.rate = tk.DoubleVar()
        self.time = tk.IntVar()
        self.result = tk.StringVar()
        self.principal_label = tk.Label(self.window, text="Principal:")
        self.principal_label.pack()
        self.principal_entry = tk.Entry(self.window, textvariable=self.principal)
        self.principal_entry.pack()
        self.rate_label = tk.Label(self.window, text="Rate:")
        self.rate_label.pack()
        self.rate_entry = tk.Entry(self.window, textvariable=self.rate)
        self.rate_entry.pack()
        self.time_label = tk.Label(self.window, text="Time:")
        self.time_label.pack()
        self.time_entry = tk.Entry(self.window, textvariable=self.time)
        self.time_entry.pack()
        self.calculate_button = tk.Button(self.window, text="Calculate", command=self.calculate_interest)
        self.calculate_button.pack()
        self.result_label = tk.Label(self.window, textvariable=self.result)
        self.result_label.pack()
        self.window.mainloop()

    def calculate_interest(self):
        principal = self.principal.get()
        rate = self.rate.get()
        time = self.time.get()
        interest = principal * (1 + rate / 100) ** time
        self.result.set(f"Interest: {interest:.2f}")

CompoundInterest()