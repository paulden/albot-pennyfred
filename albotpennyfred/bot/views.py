from django.shortcuts import render
from django.http import JsonResponse
from .services import get_weather, get_directions, post_reminder
from .serializers import LogSerializer, ReminderSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json


def weather(request, city):
    """
    Retrieves the current weather in a city calling OpenWeatherMap
    """
    data = json.loads(get_weather(city))
    return JsonResponse(data)


def directions(request, origin, dest):
    """
    Retrieves the duration of a trip calling Google Directions
    """
    data = json.loads(get_directions(origin, dest))
    return JsonResponse(data)


@api_view(['POST'])
def record_log(request):
    """
    Creates an entry in logs to record streamed tweets
    TODO: Authentication required
    """
    if request.method == 'POST':
        serializer = LogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def plan_tweet(request):
    """
    Post a tweet in Buffer account linked to Twitter with a scheduled date and time
    to remind user of their task
    TODO: Authentication required
    """
    if request.method == 'POST':
        serializer = ReminderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            p = post_reminder(serializer.data["client_id"], serializer.data["text"], serializer.data["plan_time"])
            if p:
                return Response(status=status.HTTP_201_CREATED)
            # TODO: Generate response if it fails to call Buffer API to schedule tweet
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
