# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('comments_text', models.TextField(verbose_name='Текст Коментария')),
                ('comments_likes', models.IntegerField(default=0)),
                ('comments_photo', models.ForeignKey(to='albums.Photo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
