from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import BlogPost, Comment
from .forms import BlogPostCommentForm


def home(request):
    posts = BlogPost.objects.all().order_by("-datetime_modified")
    context = {"posts": posts}
    return render(request, "index.html", context)


@login_required
def add(request):
    if request.method == "POST":
        user = request.user
        name = request.POST.get("name")
        description = request.POST.get("description")
        print(user)
        p = BlogPost.objects.create(
            title=name,
            description=description,
            author=user,
        )
        print(p)
    elif request.method == "GET":
        print(request.POST)
    return render(request, "add.html")


def detail(request, pk):
    # post = BlogPost.objects.get(pk=pk)
    post = get_object_or_404(BlogPost, pk=pk)
    comments = Comment.objects.filter(post=post)
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email", None)
        address = request.POST.get("address", "")
        city = request.POST.get("city", "")
        province = request.POST.get("state", "")
        zip_code = request.POST.get("zipcode", "")
        hide_name = request.POST.get("hide_name")
        hide_name = True if hide_name else False
        text = request.POST.get("text")
        Comment.objects.create(
            name=name,
            email=email,
            address=address,
            city=city,
            province=province,
            zip_code=zip_code,
            hide_name=hide_name,
            comment=text,
            post=post,
        )
    context = {"post": post, "comments": comments}
    return render(request, "detail.html", context)


def detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    comments = Comment.objects.filter(post=post)
    form = BlogPostCommentForm()
    if request.method == "POST":
        form = BlogPostCommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post = post
            form.save()
            form = BlogPostCommentForm()
    context = {"post": post, "comments": comments, "form": form}
    return render(request, "detail.html", context)


def recent_posts(request):
    posts = BlogPost.objects.all().order_by("-datetime_modified")[:5]
    context = {"posts": posts}
    return render(request, "index.html", context)
