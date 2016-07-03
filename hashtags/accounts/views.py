from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    return HttpResponse('<span class="testLogin">login page</span>')
