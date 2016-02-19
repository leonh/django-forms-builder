# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-09 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_auto_20160209_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='choices',
            field=models.CharField(blank=True, help_text="Comma separated options where applicable. If an option itself contains commas, surround the option starting with the 'character and ending with the ' character.", max_length=1000, verbose_name='Choices'),
        ),
        migrations.AlterField(
            model_name='field',
            name='default',
            field=models.CharField(blank=True, max_length=20000, verbose_name='Default value'),
        ),
        migrations.AlterField(
            model_name='fieldentry',
            name='value',
            field=models.CharField(max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='Slug'),
        ),
    ]
