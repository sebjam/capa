from django.core.urlresolvers import reverse
from django.test import TestCase

from gallery.models import Gallery
from model_mommy import mommy


class GalleryViewsTest(TestCase):

    def setUp(self):
        self.gallery = mommy.make(Gallery)

    def test_gallery_detail_view(self):
        response = self.client.get(
            reverse('detail_gallery', kwargs={'pk': self.gallery.id})
        )
        self.assertEqual(response.status_code, 200)
