from django.conf.urls import patterns, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
]
