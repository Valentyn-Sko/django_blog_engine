from django.shortcuts import render, redirect
from django.views.generic import View

from .models import Post
from .models import Tag
from .utils import ObjectDetailMixin,ObjectCreateMixin
from .forms import TagForm, PostForm


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'
    #def get(self, request):
    #    form = TagForm()
    #    return render(request, 'blog/tag_create.html', context={'form': form})
    #
    #def post(self, request):
    #    bound_form = TagForm(request.POST)
    #
    #    if bound_form.is_valid():
    #        new_tag = bound_form.save()
    #        return redirect(new_tag)
    #    else:
    #        return render(request, 'blog/tag_create.html', context={'form': bound_form})


class PostCreate(View):
    form_model = PostForm
    template = 'blog/post_create_form.html'
    #def get(self, request):
    #    form = PostForm()
    #    return render(request, 'blog/post_create_form.html', context={'form': form})
    #
    #def post(self, request):
    #    bound_form = PostForm(request.POST)
    #    print(PostForm)
    #    if bound_form.is_valid():
    #        new_post = bound_form.save()
    #        return redirect(new_post)
    #    else:
    #        return render(request, 'blog/post_create_form.html', context={'form': bound_form})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})
