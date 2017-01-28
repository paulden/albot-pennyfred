from django.shortcuts import render
from django.http import JsonResponse
from .services import get_weather, get_directions
import json


def weather(request, city):
    # TODO: Serialize if need be stream in a Weather object
    data = json.loads(get_weather(city))
    return JsonResponse(data)


def directions(request, origin, dest):
    # TODO: Serialize if need be directions in an object
    data = json.loads(get_directions(origin, dest))
    return JsonResponse(data)