from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .services import get_weather, get_directions
from .serializers import LogSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import collections


def weather(request, city):
    # TODO: Serialize if need be stream in a Weather object
    data = json.loads(get_weather(city))
    return JsonResponse(data)


def directions(request, origin, dest):
    # TODO: Serialize if need be directions in an object
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
