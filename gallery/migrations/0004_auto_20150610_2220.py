# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_gallery_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery',
            old_name='user',
            new_name='owner',
        ),
        migrations.AlterField(
            model_name='photo',
            name='gallery',
            field=models.ForeignKey(related_name='photos', to='gallery.Gallery'),
        ),
    ]
