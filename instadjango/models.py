from django.db import models

class InstagramMedia(models.Model):
    low_url = models.URLField()
    link = models.URLField()
    caption = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=5, blank=True, null=True)
