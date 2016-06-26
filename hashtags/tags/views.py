from django.shortcuts import render
from tags.forms import SearchForm
from tags.models import Tag


def post_list(request, tag):
    tag = Tag.objects.get(tag=tag)
    posts = tag.post.all()

    return render(request, 'tags/post_list.html', {
        'form': SearchForm(),
        'posts': posts,
    })
