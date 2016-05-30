from django.shortcuts import render

from posts.models import Post, Tag
from posts.forms import SearchForm


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

    return render(request, 'home.html', {
        'posts': Post.objects.all(),
        'form': SearchForm()
    })
