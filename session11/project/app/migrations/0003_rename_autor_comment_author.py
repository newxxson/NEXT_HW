# Generated by Django 3.2.18 on 2023-04-30 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20230430_1230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='autor',
            new_name='author',
        ),
    ]
