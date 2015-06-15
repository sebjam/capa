from django.conf import settings
from boto.s3.connection import S3Connection

conn = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
