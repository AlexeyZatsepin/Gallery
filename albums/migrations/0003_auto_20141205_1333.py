# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('comments_text', models.TextField(verbose_name='Текст Коментария')),
                ('comments_likes', models.IntegerField(default=0)),
                ('comments_photo', models.ForeignKey(to='albums.Photo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='comments',
            name='comments_photo',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
