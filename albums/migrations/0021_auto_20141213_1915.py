# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0020_auto_20141212_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 19, 15, 19, 854083)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='album',
            name='img',
            field=models.ImageField(verbose_name='Изображение альбома', upload_to='images', help_text='Желательно 250px на 250px'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='comments_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 19, 15, 19, 865084)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='img',
            field=models.ImageField(verbose_name='Фото', upload_to='images'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 19, 15, 19, 860083)),
            preserve_default=True,
        ),
    ]
