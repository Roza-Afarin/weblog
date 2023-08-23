from django.contrib import admin
from django.urls import path
###
from blog.views import *
app_name = 'blog'

urlpatterns = [
    path('',blog_index,name='blog'),
    path('<int:pk>',blog_detail,name='detail'),
    path('category/<str:cat_name>',blog_index,name='category'),
    path('author/<str:author_username>',blog_index,name='author'),
    path('tag/<str:tag_name>',blog_index,name='tag'),
    path('search/',blog_search,name='search'),
]