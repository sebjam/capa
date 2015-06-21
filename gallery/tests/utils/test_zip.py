import os

from django.contrib.auth import get_user_model

from gallery.models import Gallery, Photo
from gallery.utils.zip import process_zipfile
from model_mommy import mommy
from unittest import TestCase
from unittest.mock import patch

User = get_user_model()

TEST_ZIP_PATH = os.path.abspath(os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "files", "test.zip"))


class MyTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='test', email='test@test.com', password='test')

        self.gallery = mommy.make(Gallery, owner=self.user)

    @patch('amazon.connection.conn.get_bucket')
    @patch('gallery.utils.zip.Key')
    def test_boto(self, mock_key, mock_get_bucket):
        photo_url = 'http://www.test.com'
        mock_get_bucket.return_value = ''
        mock_key.return_value.generate_url.return_value = photo_url

        photo = Photo.objects.filter(title='test.png-1').exists()
        self.assertFalse(photo)

        process_zipfile(TEST_ZIP_PATH, self.gallery)

        photo = Photo.objects.filter(title='test.png-1').exists()
        self.assertTrue(photo)
