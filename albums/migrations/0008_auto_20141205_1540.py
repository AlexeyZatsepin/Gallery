# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0007_auto_20141205_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 5, 15, 40, 31, 656293)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='comments_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 5, 15, 40, 31, 659293)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 5, 15, 40, 31, 658293)),
            preserve_default=True,
        ),
    ]
