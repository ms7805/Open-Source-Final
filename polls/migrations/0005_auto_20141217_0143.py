# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_userprofile_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_title',
            field=models.CharField(default=b'No Topic', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(to='polls.UserProfile', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='website',
            field=models.URLField(default=None, blank=True),
            preserve_default=True,
        ),
    ]
