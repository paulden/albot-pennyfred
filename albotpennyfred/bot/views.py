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
from .services import get_weather
import json

def weather(request):
    stream = json.loads(get_weather("Brussels"))
    return JsonResponse(stream)
