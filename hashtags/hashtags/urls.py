from django.conf.urls import patterns, include, url
from django.contrib import admin

import hashtags.views

urlpatterns = [
    url(r'^$', hashtags.views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
]
