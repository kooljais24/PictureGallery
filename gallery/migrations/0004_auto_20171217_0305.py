# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-16 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_upload_photo_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload_photo',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
