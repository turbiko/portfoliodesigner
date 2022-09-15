from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-*&x)0kf4c0ed%18_@bbu0s+v5akech-2q*ro&z^lt5@wucm1x!"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["127.0.0.1", "design.argentum.ua", "10.1.100.222", "localhost" ]
CSRF_TRUSTED_ORIGINS = ['https://design.argentum.ua']

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
