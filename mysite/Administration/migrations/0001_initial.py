# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 01:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('nombreProyecto', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('csvArchive', models.FileField(upload_to=b'')),
            ],
        ),
    ]
