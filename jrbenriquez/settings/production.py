from .base import *

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

DJANGO_SETTINGS_MODULE = env("DJANGO_SETTINGS_MODULE")

# Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
# and renames the files with unique names for each version to support long-term caching
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

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
