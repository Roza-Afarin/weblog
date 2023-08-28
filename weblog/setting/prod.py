from weblog.settings import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2gh)(hd$&x7ojvck#_zo@iulhrpp_rqrv%mz6c_h3an#had1&e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['rozafarin.com','www.rozafarin.com']


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rozafari_travel',
        'USER': 'rozafari_afarin',
        'PASSWORD': 'Roza136345%',
        'HOST':'localhost',
        'PORT':'3306',
    }
}

STATIC_ROOT = 'home/rozafari/public_html/static'
MEDIA_ROOT = 'home/rozafari/public_html/media'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

SESSION_COOKIE_SECURE=True