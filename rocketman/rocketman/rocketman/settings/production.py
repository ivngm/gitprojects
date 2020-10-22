from .base import *

DEBUG = False
SECRET_KEY = 'nl3w4fvy(&!q5)8z04x$mc%bd-)x&du8au2vuc7-9jj3dn=2$t'
ALLOWED_HOSTS =['localhosto', 'rocketman.learnwagtail.com', '*']
DATABASES={
    "default":{
        "ENGINE":'django.db.backends.postgresql_pssycopg2',
        "NAME":'rocketman',
        "USER":'rocketman',
        "PASSWORD":'escape',
        "HOST":'localhost',
        "PORT": "",
    }
}

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://7e0111960ab6460ba1c55f48d34d745d@o465260.ingest.sentry.io/5477626",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

try:
    from .local import *
except ImportError:
    pass
