# Generated by Django 4.0 on 2022-05-10 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MASH_app', '0004_alter_video_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='data',
            new_name='note',
        ),
    ]
