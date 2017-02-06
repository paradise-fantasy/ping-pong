# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 22:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.TextField()),
                ('cardid', models.TextField()),
                ('profile_picture', models.URLField(blank=True, default='')),
                ('games_played', models.IntegerField(default=0)),
                ('games_won', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=1000)),
            ],
        ),
    ]
