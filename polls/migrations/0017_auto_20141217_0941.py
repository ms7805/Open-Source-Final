# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_auto_20141217_0716'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='tag',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='choice',
            name='ans_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 17, 14, 41, 19, 178000, tzinfo=utc), verbose_name=b'date published', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='choice',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 17, 14, 41, 19, 178000, tzinfo=utc), verbose_name=b'date modified', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 17, 14, 41, 19, 177000, tzinfo=utc), verbose_name=b'date modified', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 17, 14, 41, 19, 177000, tzinfo=utc), verbose_name=b'date published', blank=True),
            preserve_default=True,
        ),
    ]
