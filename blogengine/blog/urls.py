from django.urls import path
from .views import *

urlpatterns = [
    path('', posts_list, name='post_list_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),  # str по умолчанию уже .
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/create', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<slug>', TagDetail.as_view(), name='tag_detail_url'),
]
