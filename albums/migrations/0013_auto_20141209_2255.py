# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('albums', '0012_auto_20141209_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comments_author',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='album',
            name='album_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 9, 22, 55, 49, 270526)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='comments_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 9, 22, 55, 49, 277527)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 9, 22, 55, 49, 273526)),
            preserve_default=True,
        ),
    ]
