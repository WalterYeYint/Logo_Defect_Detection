# Generated by Django 4.0.2 on 2022-02-11 09:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Database_app', '0002_auto_20210908_1315'),
    ]

    operations = [
        migrations.RenameField(
            model_name='violations',
            old_name='photo',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='violations',
            old_name='behaviour',
            new_name='result',
        ),
        migrations.RemoveField(
            model_name='violations',
            name='camera_number',
        ),
        migrations.RemoveField(
            model_name='violations',
            name='name',
        ),
        migrations.RemoveField(
            model_name='violations',
            name='video',
        ),
        migrations.AlterField(
            model_name='violations',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
