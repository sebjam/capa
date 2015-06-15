from django.conf import settings
from django.contrib.postgres.fields import HStoreField
from django.db import models

from s3direct.fields import S3DirectField


class Gallery(models.Model):
    title = models.CharField(max_length=55)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

    def __unicode__(self):
        return u'{}'.format(self.title)


class Photo(models.Model):
    title = models.CharField(max_length=55)
    description = models.TextField(blank=True)
    parent = models.ForeignKey(Gallery, related_name='photos')
    image = S3DirectField(dest='imgs', default='')
    metadata = HStoreField(null=True, blank=True)
