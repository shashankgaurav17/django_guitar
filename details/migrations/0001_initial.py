# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('song_name', models.CharField(max_length=200)),
                ('cappo', models.CharField(max_length=10)),
                ('language', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=10)),
                ('url', models.CharField(max_length=200)),
                ('lyrics', models.CharField(max_length=2000)),
            ],
        ),
    ]
