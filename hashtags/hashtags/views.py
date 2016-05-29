from django.shortcuts import render

from posts.models import Post
from posts.forms import SearchForm


def home(request):
    return render(request, 'home.html', {
        'posts': Post.objects.all(),
        'form': SearchForm()
    })
