import os
from io import BytesIO
import zipfile

from django.conf import settings
from amazon.connection import conn
from boto.s3.key import Key
from gallery.models import Photo
from PIL import Image


def process_zipfile(file_path, gallery):
    bucket = conn.get_bucket(settings.AWS_STORAGE_BUCKET_NAME)
    if os.path.isfile(file_path):
        zip = zipfile.ZipFile(file_path)
        bad_file = zip.testzip()
        if bad_file:
            raise Exception('"%s" in the .zip archive is corrupt.' % bad_file)
        count = 1
        for filename in sorted(zip.namelist()):
            data = zip.read(filename)
            string_buffer = BytesIO(data)
            if len(data):
                try:
                    # load() is the only method that can spot a truncated JPEG,
                    # but it cannot be called sanely after verify()
                    trial_image = Image.open(string_buffer)
                    trial_image.load()
                    # verify() is the only method that can spot a corrupt PNG,
                    #  but it must be called immediately after the constructor
                    trial_image = Image.open(string_buffer)
                    trial_image.verify()
                except Exception:
                    # if a "bad" file is found we just skip it.
                    continue
                while 1:
                    title = '{}-{}'.format(filename, str(count))
                    key = Key(bucket)
                    key.key = title
                    key.set_contents_from_file(string_buffer)
                    url = key.generate_url(
                        expires_in=0,
                        query_auth=False,
                        force_http=True
                    )
                    photo = Photo(
                        parent=gallery,
                        title=title,
                        image=url
                    )
                    photo.save()
                    count = count + 1
                    break
                count = count + 1
        zip.close()
        return True
