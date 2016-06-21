# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers

from posts.models import Post, Tag
from posts.forms import SearchForm

import json


def home(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            tag_query = form.cleaned_data['search_tag']
            tag = Tag.objects.get(tag=tag_query)
            posts = tag.post.all()

            return render(request, 'posts.html', {
                'posts': posts,
                'form': SearchForm()
            })

    if request.is_ajax() and request.GET.get('term'):
        return HttpResponse(
            json.dumps({'result': 'test'}),
            'application/json'
        )
    return render(request, 'home.html', {
        'posts': Post.objects.all(),
        'form': SearchForm()
    })
