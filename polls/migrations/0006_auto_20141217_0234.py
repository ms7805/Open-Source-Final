# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20141217_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 17, 7, 34, 43, 201000, tzinfo=utc), verbose_name=b'date published', blank=True),
            preserve_default=True,
        ),
    ]
