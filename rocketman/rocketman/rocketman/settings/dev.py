import os
from .base import *
import debug_toolbar
from django.conf import settings
from django.urls import include, path

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ooadm_5b070a0g+g6at3@fv_z3ix5#ce14p&=dh&i@ke-hhpi$'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE +=[
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',
]

cwd= os.getcwd()

CACHES = {
    "default":{
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": f"{cwd}/.cache"
    }
}
try:
    from .local import *
except ImportError:
    pass
