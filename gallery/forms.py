from django import forms
from s3direct.widgets import S3DirectWidget

class S3DirectUploadForm(forms.Form):
    title = forms.CharField(label='Title')
    description = forms.CharField(label='Title')
    gallery = forms.ModelChoiceField()
    image = forms.URLField(widget=S3DirectWidget(dest='destination_key_from_settings')
