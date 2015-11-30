__author__ = 'Valentyn'
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [


    url(r'^$', 'data_input.views.parser', name='parser'),
]