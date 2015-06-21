import os
from .base import *

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'capa',
        'USER': 'capa',
        'PASSWORD': os.environ['CAPA_DB_PASSWORD'],
        'HOST': 'localhost',
        'PORT': os.environ.get('CAPA_DB_PORT', ''),
    }
}
