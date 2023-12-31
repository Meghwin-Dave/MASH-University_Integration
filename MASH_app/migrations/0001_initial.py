# Generated by Django 4.0 on 2022-03-25 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(default='', max_length=25)),
            ],
            options={
                'db_table': 'Faculty',
            },
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Password', models.CharField(max_length=20)),
                ('IsActive', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Master',
            },
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Role', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Role',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(null=True, upload_to='images_uploaded')),
                ('video', models.FileField(null=True, upload_to='videos_uploaded')),
                ('date_uploaded', models.DateTimeField()),
                ('Faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MASH_app.faculty')),
            ],
            options={
                'db_table': 'Video',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UID', models.CharField(max_length=25)),
                ('FullName', models.CharField(default='', max_length=25)),
                ('Enrollment', models.CharField(max_length=12)),
                ('Master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MASH_app.master')),
            ],
            options={
                'db_table': 'User',
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=550)),
                ('Faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MASH_app.faculty')),
            ],
            options={
                'db_table': 'Note ',
            },
        ),
        migrations.AddField(
            model_name='master',
            name='Role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MASH_app.role'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='Master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MASH_app.master'),
        ),
        migrations.CreateModel(
            name='Assign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assign', models.FileField(default='xyz.png', upload_to='assignments/')),
                ('Faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MASH_app.faculty')),
            ],
            options={
                'db_table': 'Assign',
            },
        ),
    ]
