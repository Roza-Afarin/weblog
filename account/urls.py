from django.contrib import admin
from django.urls import path
from account.views import ResetPasswordView

###
from . import views
app_name = 'account'

urlpatterns = [
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('signup',views.signup_view,name='signup'),
     path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
     

]