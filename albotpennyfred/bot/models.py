from django.db import models


class Log(models.Model):
    id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=60)
    text = models.TextField()
    time = models.CharField(max_length=40)

    def __str__(self):
        return self.text
