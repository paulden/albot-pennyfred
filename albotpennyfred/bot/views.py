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


def get_weather(request):
    if request.method == "GET":
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Brussels&units=metric&appid='
                         + settings.OPENWEATHERMAP_KEY)
        json = r.json()
        print(json)
        serializer = WeatherSerializer(data=json)
        if serializer.is_valid():
            # weather = serializer.save()
            print("all good")
            return JsonResponse(serializer.data)
