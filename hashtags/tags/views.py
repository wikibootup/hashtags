from django.shortcuts import render
from tags.forms import SearchForm


def post_list(request, tag):
    return render(request, 'tags/post_list.html', {
        'form': SearchForm()
    })
