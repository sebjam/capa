from django.db import models
from s3direct.fields import S3DirectField

class Gallery(models.Model):
    title = models.CharField(max_length=55)
    description = models.TextField(blank=True)

class Photo(models.Model):
    title = models.CharField(max_length=55)
    description = models.TextField(blank=True)
    gallery = models.ForeignKey(Gallery)
    image = S3DirectField(dest='imgs', default='')
