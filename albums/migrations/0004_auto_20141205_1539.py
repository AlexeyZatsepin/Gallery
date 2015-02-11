# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0003_auto_20141205_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 5, 15, 39, 15, 532939)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='album',
            name='album_likes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='comments_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 5, 15, 39, 15, 535939)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photo',
            name='photo_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 5, 15, 39, 15, 534939)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photo',
            name='photo_likes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterModelTable(
            name='album',
            table='Album',
        ),
    ]
