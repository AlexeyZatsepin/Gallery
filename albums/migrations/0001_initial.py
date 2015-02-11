# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='Название альбома', max_length=100)),
                ('slug', models.SlugField(verbose_name='Ссылка для альбома', unique=True, max_length=100)),
                ('img', models.ImageField(help_text='Размер изображения 200px на 200px', verbose_name='Изображение альбома', upload_to='images')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='Название фотографии', max_length=100)),
                ('img', models.ImageField(help_text='Желательно, чтоб фото было не большого размера', verbose_name='Фото', upload_to='images')),
                ('album', models.ForeignKey(to='albums.Album', verbose_name='Альбом')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
