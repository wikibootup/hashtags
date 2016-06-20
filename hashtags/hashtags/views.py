# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

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

    if request.is_ajax():
        if request.GET['term']:
            result = Tag.objects.filter(tag__istartswith=request.GET['term'])
            if not result:
                not_found = '검색 결과가 없습니다.'
                return HttpResponse(
                    json.dumps({'result': not_found}),
                    'application/json'
                )
            return HttpResponse(
                    json.dumps({'result': result}),
                    'application/json'
            )
        else:
            return HttpResponse(
                json.dumps({'result': ''}),
                'application/json'
            )

    return render(request, 'home.html', {
        'posts': Post.objects.all(),
        'form': SearchForm()
    })
