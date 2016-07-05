from django.conf.urls import patterns, url
from django.contrib import admin

import tags.views

urlpatterns = [
    url(r'^(?P<tag>[\w\-]+)/$', tags.views.post_list, name='post_list'),
]
