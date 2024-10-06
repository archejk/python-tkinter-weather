import requests
import tkinter as tk
from tkinter import messagebox
from dotenv import load_dotenv
import os

load_dotenv()

# set up API key and base URL
API_KEY = os.getenv('WEATHER_API_KEY')
BASE_URL = "http://api.weatherapi.com/v1/current.json"

# def a function to get weather data
def get_weather(city_name):
    complete_url = f"{BASE_URL}?key={API_KEY}&q={city_name}&aqi=no"
    
    try:
        response = requests.get(complete_url)

        print(f"response URL: {response.url}")
        print(f"response status code: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            location = data['location']
            current = data['current']
            
            print(f"response data: {data}")
            
            result = f"City: {location['name']}, {location['country']}\n"
            result += f"Temperature: {current['temp_c']}°C\n"
            result += f"Humidity: {current['humidity']}%\n"
            result += f"Weather: {current['condition']['text']}\n"
            result += f"Wind Speed: {current['wind_kph']} kph"
            
            # display the result in the label
            result_label.config(text=result)
        else:
            print(f"Error: {response.json()}")
            messagebox.showerror("Error", f"City of {city_name} not found!")
    
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Network Error", str(e))

# create the main window
root = tk.Tk()
root.title("Weather Dashboard")

# create input field and button
city_entry = tk.Entry(root, width=100)
city_entry.pack(pady=50)
city_entry.insert(0, "Enter city name")

get_weather_button = tk.Button(root, text="Get Weather", command=lambda: get_weather(city_entry.get()))
get_weather_button.pack(pady=50)

# create a label to display the result
result_label = tk.Label(root, text="", font=("Helvetica", 15))
result_label.pack(pady=50)

# run the Tkinter event loop
root.mainloop()
