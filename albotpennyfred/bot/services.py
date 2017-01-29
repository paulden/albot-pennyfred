import requests
import json

access_token_buffer = "xxx"
# Variables that contain other API keys
openweathermap_key = "xx"
googleapi_key = "xxx"


# TODO: Catch exceptions where functions fail to return proper Json files


def get_weather(city):
    result = {}
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'units': 'metric', 'appid': openweathermap_key}
    r = requests.get(url, params=params)
    forecast = r.json()
    result["desc"] = forecast["weather"][0]["description"]
    result["temperature"] = forecast["main"]["temp"]
    result["location"] = forecast["name"]
    return json.dumps(result)


def get_directions(origin, dest):
    result = {}
    url = 'https://maps.googleapis.com/maps/api/directions/json'
    params = {'origin': origin, 'destination': dest, 'key': googleapi_key}
    r = requests.get(url, params=params)
    directions = r.json()
    result["duration"] = directions["routes"][0]['legs'][0]["duration"]["text"]
    return json.dumps(result)


def post_reminder(buffer_id, text, time):
    url = 'https://api.bufferapp.com/1/updates/create.json'
    params = {'text': text, 'profile_ids': buffer_id, 'scheduled_at': time, 'access_token': access_token_buffer}
    r = requests.post(url, params)
    result = r.json()
    print(result)
    if "success" in result:
        return result["success"]
