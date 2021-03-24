from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'all_posts': posts})


def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog-post-1.html', {'post': post})
