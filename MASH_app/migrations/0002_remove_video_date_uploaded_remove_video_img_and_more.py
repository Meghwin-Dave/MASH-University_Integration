# Generated by Django 4.0 on 2022-05-09 14:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MASH_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='date_uploaded',
        ),
        migrations.RemoveField(
            model_name='video',
            name='img',
        ),
        migrations.RemoveField(
            model_name='video',
            name='video',
        ),
        migrations.AddField(
            model_name='video',
            name='link',
            field=models.CharField(default=' ', max_length=550),
            preserve_default=False,
        ),
    ]
