from .base import *

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

DJANGO_SETTINGS_MODULE = env("DJANGO_SETTINGS_MODULE")

# Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
# and renames the files with unique names for each version to support long-term caching
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

INSTALLED_APPS += [
    "storages",
]

# Cloudflare R2 S3 Storage Settings
AWS_S3_ACCESS_KEY_ID = env("R2_ACCESS_KEY_ID")
AWS_S3_SECRET_ACCESS_KEY = env("R2_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
AWS_S3_ENDPOINT_URL = env("AWS_S3_ENDPOINT_URL") # 
AWS_S3_ADDRESSING_STYLE = "virtual"  # Uses bucket as a subdomain
AWS_S3_SIGNATURE_VERSION = "s3v4"  # Explicitly enforce SigV4

# Set default storage backend for production
STORAGES["default"] = {
    "BACKEND": "storages.backends.s3.S3Storage",
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
