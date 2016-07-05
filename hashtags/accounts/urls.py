from django.conf.urls import patterns, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(), name='login'),
]
