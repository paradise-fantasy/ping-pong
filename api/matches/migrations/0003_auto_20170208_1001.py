# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 10:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0002_auto_20170208_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='player_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_1', to='players.Player'),
        ),
        migrations.AlterField(
            model_name='match',
            name='player_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_2', to='players.Player'),
        ),
    ]
