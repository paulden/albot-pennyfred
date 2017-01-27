from django.conf.urls import url
from bot import views

urlpatterns = [
    # url(r'^weather/$', views.weather),
    url(r'^weather/(?P<city>[a-zA-Z]+)/$', views.weather),  # TODO: Use a more comprehensive RegEx
    url(r'^directions/(?P<origin>[a-zA-Z]+)/(?P<dest>[a-zA-Z]+)/$', views.directions)
]