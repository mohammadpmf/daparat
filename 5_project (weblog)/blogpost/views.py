from django.shortcuts import render, get_object_or_404

from .models import BlogPost


def home(request):
    posts = BlogPost.objects.all()
    context = {"posts": posts}
    return render(request, "index.html", context)


def add(request):
    return render(request, "add.html")


def detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    context = {"post": post}
    return render(request, "detail.html", context)
