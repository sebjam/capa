from rest_framework import serializers
from .models import Gallery, Photo


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'title', 'description', 'image')


class GallerySerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Gallery
        fields = ('title', 'description', 'user')
