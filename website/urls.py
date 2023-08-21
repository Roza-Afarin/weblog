from django.contrib import admin
from django.urls import path
from website.views import *
app_name = 'website'

urlpatterns = [
    path('',home_index,name='index'),
    path('about',about_index,name='about'),
    path('contact',contact_index,name='contact'),
]