from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from bot import views

urlpatterns = [
    # url(r'^weather/$', views.weather),
    url(r'^weather/(?P<city>[a-zA-Z]+)/$', views.weather),  # TODO: Use a more comprehensive RegEx
    url(r'^directions/(?P<origin>[a-zA-Z]+)/(?P<dest>[a-zA-Z]+)/$', views.directions),  # TODO: Same here
    url(r'^record_log/$', views.record_log)
]

urlpatterns = format_suffix_patterns(urlpatterns)