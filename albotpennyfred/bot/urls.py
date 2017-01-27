from django.conf.urls import url
from bot import views

urlpatterns = [
    url(r'^weather/$', views.weather),
]