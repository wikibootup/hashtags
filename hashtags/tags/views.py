from django.shortcuts import render


def post_list(request, tag):
    return render(request, 'tags/post_list.html')
