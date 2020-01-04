from django.urls import path
from .views import *

urlpatterns = [
    path('', posts_list, name='post_list_url'),
    path('post/<str:slug>/', post_detail, name='post_detail_url'),  # str по умолчанию уже .
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/<slug>', tag_detail, name='tag_detail_url')
]
