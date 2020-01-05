from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import get_object_or_404

# Create your views here.
from .models import Post
from .models import Tag


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower: obj})
