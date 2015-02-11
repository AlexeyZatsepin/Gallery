# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0010_auto_20141205_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 5, 16, 12, 26, 578820)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='comments_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 5, 16, 12, 26, 580820)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 5, 16, 12, 26, 579820)),
            preserve_default=True,
        ),
    ]
