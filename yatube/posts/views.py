from django.shortcuts import get_object_or_404, render

from .consts import POSTS_IN_PAGE
from .models import Group, Post


def index(request):
    posts = Post.objects.all()[:POSTS_IN_PAGE]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:POSTS_IN_PAGE]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
