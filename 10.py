import tkinter as tk
import requests

class WeatherApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Weather App")
        self.city = tk.StringVar()
        self.city_label = tk.Label(self.window, text="Enter city:")
        self.city_label.pack()
        self.city_entry = tk.Entry(self.window, textvariable=self.city)
        self.city_entry.pack()
        self.get_weather_button = tk.Button(self.window, text="Get Weather", command=self.get_weather)
        self.get_weather_button.pack()
        self.weather_label = tk.Label(self.window, text="")
        self.weather_label.pack()
        self.window.mainloop()

    def get_weather(self):
        city = self.city.get()
        if city:
            response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY")
            if response.status_code == 200:
                weather_data = response.json()
                self.weather_label.config(text=f"Weather in {city}: {weather_data['weather'][0]['description']}")
            else:
                messagebox.showerror("Error", "Failed to get weather data")
        else:
            messagebox.showerror("Error", "Please enter a city")

WeatherApp()