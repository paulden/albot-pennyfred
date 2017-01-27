from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Weather
from .serializers import WeatherSerializer
from django.conf import settings
import requests
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