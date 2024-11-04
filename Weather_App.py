import requests 
import tkinter as tk
from tkinter import messagebox
def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    if location.isdigit():
        params = {'zip': f'{location},IN', 'appid': api_key, 'units': 'metric'}
    else:
        params = {'q': f'{location},IN', 'appid': api_key, 'units': 'metric'}
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        weather_info = {
            "City": data["name"],
            "Temperature": main["temp"],
            "Humidity": main["humidity"],
            "Weather": weather["description"].capitalize()
        }
        return weather_info
    else:
        return None
def show_weather():
    location = location_entry.get()
    api_key = "22af4c9d4c6d00ef743a4c3ce76e92ff"  
    weather = get_weather(api_key, location)
    if weather:
        result = (f"City: {weather['City']}\n"
        f"Temperature: {weather['Temperature']}°C\n"
        f"Humidity: {weather['Humidity']}%\n"
        f"Weather: {weather['Weather']}")
        weather_label.config(text=result)
    else:
        messagebox.showerror("Error", "City name or zip code not found. Please try again.")
app = tk.Tk()
app.title("Weather App")
app.geometry("300x250")
location_label = tk.Label(app, text="Enter City Name or Zip Code:")
location_label.pack(pady=10)
location_entry = tk.Entry(app, width=20)
location_entry.pack()
get_weather_button = tk.Button(app, text="Get Weather", command=show_weather)
get_weather_button.pack(pady=10)
weather_label = tk.Label(app, text="", font=("Arial", 12), justify="left")
weather_label.pack(pady=10)
app.mainloop()
