from django.db import models


class Log(models.Model):
    id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=60)
    text = models.CharField(max_length=200)
    time = models.CharField(max_length=20)

    class Meta:
        ordering = ('time',)

    def __str__(self):
        return self.text
