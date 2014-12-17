# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20141217_0234'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='choice_title',
            field=models.CharField(default=b'No Title', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='choice',
            name='creator',
            field=models.ForeignKey(to='polls.UserProfile', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='votes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 17, 7, 49, 56, 637000, tzinfo=utc), verbose_name=b'date published', blank=True),
            preserve_default=True,
        ),
    ]
