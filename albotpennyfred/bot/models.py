from django.db import models


class Log(models.Model):
    id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=60)
    text = models.CharField(max_length=250)
    time = models.CharField(max_length=40)

    def __str__(self):
        return self.text


class Reminder(models.Model):
    id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    text = models.CharField(max_length=250)
    plan_time = models.CharField(max_length=100)
    client_id = models.CharField(max_length=100)

    def __str__(self):
        return self.text
