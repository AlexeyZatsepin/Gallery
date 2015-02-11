# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avatar',
            name='avatar_user',
        ),
        migrations.DeleteModel(
            name='Avatar',
        ),
    ]
