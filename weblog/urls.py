"""
URL configuration for weblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemap
from blog.sitemaps import BlogSitemap
from django.contrib.auth import views as auth_views




sitemaps = {
    "static": StaticViewSitemap,
    'blog': BlogSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('website.urls')),
    path('blog/',include('blog.urls')),
    path('captcha/', include('captcha.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('account/',include('account.urls')),
    path(
            "sitemap.xml",
            sitemap,
            {"sitemaps": sitemaps},
            name="django.contrib.sitemaps.views.sitemap",
        ),
    path('robots.txt', include('robots.urls')),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),
         path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html',),
         name='password_reset_complete'),
]
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'website.views.custom_404'