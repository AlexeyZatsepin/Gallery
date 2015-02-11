# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0019_auto_20141211_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 12, 23, 26, 28, 800010)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='comments_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 12, 23, 26, 28, 807011)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 12, 23, 26, 28, 804010)),
            preserve_default=True,
        ),
    ]
