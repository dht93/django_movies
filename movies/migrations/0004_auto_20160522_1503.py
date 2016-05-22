# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20160522_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdb_rating',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster_url',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tomatometer',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
