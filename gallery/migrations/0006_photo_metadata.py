# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields.hstore
from django.contrib.postgres.operations import HStoreExtension


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_auto_20150611_2247'),
    ]

    operations = [
        HStoreExtension(),
        migrations.AddField(
            model_name='photo',
            name='metadata',
            field=django.contrib.postgres.fields.hstore.HStoreField(null=True, blank=True),
        ),
    ]
