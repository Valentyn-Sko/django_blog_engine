from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import get_object_or_404

# Create your views here.
from .models import Post
from .models import Tag
from .utils import ObjectDetailMixin


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


class PostDetail(ObjectDetailMixin, View):
    # def get(self, request, slug): #used before mixin
    #    post = get_object_or_404(Post, slug__iexact=slug)
    #    #post = Post.objects.get(slug__iexact=slug) change to get_object_or_404
    #    return render(request, 'blog/post_detail.html', context={'post': post})
    model = Post
    template = 'blog/post_detail.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'
    # def get(self, request, slug):  #used before mixin
    #    #tag = Tag.objects.get(slug__iexact=slug) change to get_object_or_404
    #    tag = get_object_or_404(Tag, slug__iexact=slug)
    #    return render(request, 'blog/tag_detail.html', context={'tag': tag})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})
