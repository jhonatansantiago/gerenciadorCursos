# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('turmaApp', '0003_escola'),
    ]

    operations = [
        migrations.AddField(
            model_name='turma',
            name='escola',
            field=models.ForeignKey(default=1, to='turmaApp.Escola'),
            preserve_default=False,
        ),
    ]
