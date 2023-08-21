from django.contrib import admin
from django.urls import path
###
from blog.views import *
app_name = 'blog'

urlpatterns = [
    path('',blog_index,name='blog'),
    path('detail',blog_detail,name='detail'),
]