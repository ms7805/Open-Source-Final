# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_auto_20141217_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(default=b'Picture', max_length=50)),
                ('image', models.ImageField(null=True, upload_to=b'photos/%Y/%m/%d', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='choice',
            name='ans_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 17, 15, 38, 30, 967000, tzinfo=utc), verbose_name=b'date published', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='choice',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 17, 15, 38, 30, 967000, tzinfo=utc), verbose_name=b'date modified', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 17, 15, 38, 30, 967000, tzinfo=utc), verbose_name=b'date modified', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 17, 15, 38, 30, 967000, tzinfo=utc), verbose_name=b'date published', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(upload_to=b'profile_images', blank=True),
            preserve_default=True,
        ),
    ]
