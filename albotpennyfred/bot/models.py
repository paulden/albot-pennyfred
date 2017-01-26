from django.db import models


class Weather(models.Model):
    date = models.DateField(auto_now_add=True)
    desc = models.CharField(max_length=40)
    temp = models.CharField(max_length=10)
    location = models.CharField(max_length=30)