import requests
import json

OPENWEATHERMAP_KEY = '95ebe617b4fcaf0f7a54f388c5bc5816'
GG_KEY = 'AIzaSyC0UwA4FXJo5KKK_3ullfhn0vHzPWHCeuc'

# TODO: Catch exceptions where functions fail to return proper Json files


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


def get_directions(origin, dest):
    result = {}
    url = 'https://maps.googleapis.com/maps/api/directions/json'
    params = {'origin': origin, 'destination': dest, 'key': GG_KEY}
    r = requests.get(url, params=params)
    directions = r.json()
    result["duration"] = directions["routes"][0]['legs'][0]["duration"]["text"]
    return json.dumps(result)

# get_directions('48.7669471,2.2811072', 'rue Lhomond')


def post_reminder(buffer_id, text, time):
    url = 'https://api.bufferapp.com/1/updates/create.json'
    params = {'text': text, 'profile_ids': buffer_id, 'scheduled_at': time, 'access_token': "1/7c5c80fb96e52c22ea1147076f63f819"}
    r = requests.post(url, params)
    result = r.json()
    print(result)
    if "success" in result:
        if result["success"] == "true":
            return True


post_reminder("588dac6e01a953bf15457145", "on retest", "1485702900.0")

# client_id = "588dae8dba8b5fa269457144"
# redirect_uri = "urn:ietf:wg:oauth:2.0:oob"
# client_secret= "684b7340bb96f0ae13782675dcaa0adc"
# grant_type= "authorization_code"
# url = "https://api.bufferapp.com/1/oauth2/token.json?"
# code = "1/ff63b21184821925371e692f972fef26"
# params = {"client_id": client_id, "client_secret": client_secret, "redirect_uri": redirect_uri, "code": code,"grant_type": grant_type}
# r = requests.post(url, params)
# result = r.json()
# print(result)
