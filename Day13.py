#!/usr/bin/env python3

print ("Using External Libraries: Requests")
print ("""Create a Python script that fetches data from a public API (e.g., OpenWeatherMap) and displays the 
weather.""")

import requests

city_name = input ("Enter name of city: ")
api_key = input ("Enter API key: ")
url = url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'

response = requests.get(url)
data = response.json()

temperature = data["main"]["temp"]
weather_description = data["weather"][0]["description"]

print(f"Weather in {city_name}:")
print(f"Temperature: {temperature}°C")
print(f"Description: {weather_description}")




