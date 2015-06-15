# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20150610_2220'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='gallery',
            new_name='parent',
        ),
    ]
