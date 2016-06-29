# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

from tags.models import Post, Tag

import json


def home(request):
    if request.is_ajax() and request.GET.get('term'):
        result = []
        tags = Tag.objects.filter(tag__istartswith=request.GET['term'])
        for tag in tags:
            tags_ = {}
            tags_['id'] = tag.id
            tags_['label'] = tag.tag
            tags_['value'] = tag.tag
            tags_['href'] = "/tags/%s" % tag.tag
            result.append(tags_)

        return HttpResponse(
            json.dumps(result),
            'application/json'
        )
    return render(request, 'home.html', {
        'posts': Post.objects.all(),
    })
