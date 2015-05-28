import os
from .base import *

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'capa',
        'USER': os.environ['CAPA_DB_PASSWORD'],
        'PASSWORD': 'capa',
        'HOST': 'localhost',
        'PORT': '',
    }
}
