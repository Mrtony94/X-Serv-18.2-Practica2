# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-18 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='url_original',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('url', models.TextField(default = "")),
            ],
        ),
    ]