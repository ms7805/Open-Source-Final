# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='website',
            field=models.URLField(default=b'', blank=True),
            preserve_default=True,
        ),
    ]
