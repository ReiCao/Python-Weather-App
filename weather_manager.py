import json

import openmeteo_requests

import requests_cache
from retry_requests import retry

cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

class WeatherManager:
    url = "https://api.open-meteo.com/v1/forecast"

    with open('coordinates.JSON', 'r') as f:
        city_list_coordinates = json.load(f)
        city_list = city_list_coordinates.keys()

    current_weather = None

    def update_weather(self, city):
        params = {
            "latitude": self.get_city_latitude(city),
            "longitude": self.get_city_longitude(city),
            "current": ["temperature_2m", "weather_code"],
        }
        responses = openmeteo.weather_api(self.url, params=params)

        response = responses[0]

        self.current_weather = response.Current()

    def __init__(self):
        self.update_weather("Sao Paulo")

    def is_city_real(self, city):
        if city in self.city_list_coordinates:
            return True
        else: return False

    def get_city_latitude(self, city):
        return self.city_list_coordinates[city][0]

    def get_city_longitude(self, city):
        return self.city_list_coordinates[city][1]

    def get_current_temp(self):
        return f'{self.current_weather.Variables(0).Value():.2f}'

    def get_current_weather_code(self):
        return self.current_weather.Variables(1).Value()

    def get_city_list(self):
        return list(self.city_list)