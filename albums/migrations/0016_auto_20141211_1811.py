# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0015_auto_20141210_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avatar',
            name='avatar_user',
        ),
        migrations.DeleteModel(
            name='Avatar',
        ),
        migrations.AlterField(
            model_name='album',
            name='album_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 11, 18, 11, 2, 576660)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='comments_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 11, 18, 11, 2, 579660)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 11, 18, 11, 2, 577660)),
            preserve_default=True,
        ),
    ]
