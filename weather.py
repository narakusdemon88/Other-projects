"""
A simple weather app using the Open Weather Map API
Built on 7/31/2021 using Python 3.9
"""

import requests


class Weather:
    def __init__(self, city_name):
        self.city_name = city_name
        # An API can be obtained by creating a free account at https://openweathermap.org/
        self.api_key = "API ID GOES HERE"

    def kelvin_to_celsius(self, kelvin_temp):
        return int(kelvin_temp - 273.15)

    def kelvin_to_fahreneheit(self, kelvin_temp):
        celsius_temp = kelvin_temp - 273.15
        return int(celsius_temp * (9 / 5) + 32)

    def get_weather(self):
        url = f"http://api.openweathermap.org/data/2.5/weather?appid={self.api_key}&q={self.city_name}"
        return requests.get(url).json()

    def display_weather_data(self):
        weather_data = self.get_weather()

        kelvin_temp = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']

        celsius_weather = self.kelvin_to_celsius(kelvin_temp)
        fahrenheit_weather = self.kelvin_to_fahreneheit(kelvin_temp)

        if description == "clear sky":
            description = "clear skies"

        return f"Right now the weather in {self.city_name.title()} is {celsius_weather}c with {description}.\n" \
               f"The weather in Fahrenheit is {fahrenheit_weather}f, and the humidity is {humidity}%."


if __name__ == "__main__":
    while True:

        print("Welcome to the Akashi Weather APP (AWA)!")
        city_name = input("Please input a city or press 'Exit' to exit: ")
        if city_name == "Exit" or city_name == "exit":
            break
        else:
            weather_results = Weather(city_name)
            print("\n" + weather_results.display_weather_data() + "\n")
