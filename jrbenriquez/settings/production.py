from .base import *

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

DJANGO_SETTINGS_MODULE = env("DJANGO_SETTINGS_MODULE")

# Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
# and renames the files with unique names for each version to support long-term caching
STORAGES["staticfiles"] = {
    "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
}

INSTALLED_APPS += [
    "storages",
]

# Set default storage backend for production
STORAGES["default"] = {
    "BACKEND": "storages.backends.s3.S3Storage",
}

if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY is required")

_hosts = [h.strip() for h in ALLOWED_HOSTS if h.strip()]
ALLOWED_HOSTS = _hosts + ["localhost", "127.0.0.1"]
CSRF_TRUSTED_ORIGINS = [f"https://{h}" for h in _hosts if h not in ("localhost", "127.0.0.1")]
WAGTAILADMIN_BASE_URL = os.getenv("WAGTAILADMIN_BASE_URL", WAGTAILADMIN_BASE_URL)

# Behind the Openship edge (TLS terminates there). Do not enable SECURE_SSL_REDIRECT:
# the container healthcheck uses plain http and the edge already redirects.
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# SQLite: WAL + long busy timeout so concurrent gunicorn workers do not lose writes.
if DATABASES["default"]["ENGINE"].endswith("sqlite3"):
    DATABASES["default"]["OPTIONS"] = {
        "timeout": 20,
        "init_command": "PRAGMA journal_mode=WAL;",
    }

try:
    from .local import *
except ImportError:
    pass


LOGGING = {  
    'version': 1,  
    'disable_existing_loggers': False,  
    'formatters': {  
        'verbose': {  
            'format': '{levelname} {asctime} {module} {message}',  
            'style': '{',  
        },  
        'simple': {  
            'format': '{levelname} {message}',  
            'style': '{',  
        },  
    },  
    'handlers': {  
        'console': {  
            'level': 'DEBUG',  
            'class': 'logging.StreamHandler',  
            'formatter': 'simple',  
        },  
        'file': {  
            'level': 'ERROR',  
            'class': 'logging.FileHandler',  
            'filename': 'error.log',  
            'formatter': 'verbose',  
        },  
    },  
    'loggers': {  
        'django': {  
            'handlers': ['console'],  
            'level': 'INFO',  
            'propagate': True,  
        },  
        'django.server': {  
            'handlers': ['console'],  
            'level': 'ERROR',  
            'propagate': False,  
        },  
        'jrbenriquez': {  
            'handlers': ['file'],  
            'level': 'ERROR',  
            'propagate': False,  
        },  
    },  
}
