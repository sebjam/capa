from django.db import models

class Gallery(models.Model):
    title = models.CharField(max_length=55)
    description = models.TextField(blank=True)

class Photo(models.Model):
    title = models.CharField(max_length=55)
    description = models.TextField(blank=True)
    gallery = models.ForeignKey(Gallery)
