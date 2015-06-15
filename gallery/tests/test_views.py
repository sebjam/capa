from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory

from gallery.models import Gallery, Photo
from gallery.views import (
    DetailGalleryView,
    DetailPhotoView,
    ListGalleryView
)

from model_mommy import mommy

User = get_user_model()


class GalleryViewsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='test', email='test@test.com', password='test')
        self.factory = RequestFactory()

        self.gallery = mommy.make(Gallery, owner=self.user)
        self.photos = mommy.make(Photo, parent=self.gallery, _quantity=10)

    def test_gallery_detail_view(self):
        kwargs = {'pk': self.gallery.id}
        request = self.factory.get(
            reverse('detail_gallery', kwargs=kwargs)
        )
        request.user = self.user
        response = DetailGalleryView.as_view()(request, **kwargs)
        self.assertEqual(response.status_code, 200)

    def test_gallery_list_view(self):
        request = self.factory.get(
            reverse('list_gallery')
        )
        request.user = self.user
        response = ListGalleryView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_photo_detail_view(self):
        kwargs = {'parent_pk': self.gallery.id, 'pk': self.photos[0].id}
        request = self.factory.get(
            reverse('detail_photo', kwargs=kwargs)
        )
        request.user = self.user
        response = DetailPhotoView.as_view()(request, **kwargs)
        self.assertEqual(response.status_code, 200)
