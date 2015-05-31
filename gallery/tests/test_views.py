from django.core.urlresolvers import reverse

from model_mommy import mommy

from gallery.models import Gallery, Photo

from rest_framework import status
from rest_framework.test import APITestCase


class GalleryViewsTest(APITestCase):

    def setUp(self):
        self.gallery = mommy.make(Gallery)
        self.photos = mommy.make(
            Photo,
            gallery=self.gallery,
            _quantity=10
        )

    def test_list_gallery_photos(self):
        response = self.client.get(reverse('photo-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # TODO: assert list of photos

    def test_list_gallery(self):
        response = self.client.get(reverse('gallery-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # TODO: assert list of photos
