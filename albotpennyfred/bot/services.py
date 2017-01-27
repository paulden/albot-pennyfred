import requests
import json

OPENWEATHERMAP_KEY = '95ebe617b4fcaf0f7a54f388c5bc5816'


def get_weather(city):
    result = {}
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'units': 'metric', 'appid': OPENWEATHERMAP_KEY}
    r = requests.get(url, params=params)
    forecast = r.json()
    result["desc"] = forecast["weather"][0]["description"]
    result["temperature"] = forecast["main"]["temp"]
    result["location"] = forecast["name"]
    return json.dumps(result)
