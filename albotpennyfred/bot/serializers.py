from rest_framework import serializers
from .models import Log, Reminder


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ('id', 'username', 'text', 'time')


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ('id', 'username', 'text', 'plan_time', 'client_id')
