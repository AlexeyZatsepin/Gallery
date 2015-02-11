# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0014_auto_20141210_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 10, 17, 44, 51, 11605)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='avatar',
            name='avatar_user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='comments_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 10, 17, 44, 51, 15605)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 10, 17, 44, 51, 13605)),
            preserve_default=True,
        ),
    ]
