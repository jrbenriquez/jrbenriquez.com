from .base import *

DEBUG = True
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-q4-2np#)&kx$=1oar7*krm(ez@ljb+@a*1nrxo8z#6u4t@kz1h"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

INSTALLED_APPS += [
    "django_browser_reload",
]

MIDDLEWARE += [
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

try:
    from .local import *
except ImportError:
    pass
