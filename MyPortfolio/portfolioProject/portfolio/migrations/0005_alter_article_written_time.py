# Generated by Django 3.2.18 on 2023-04-06 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_article_article_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='written_time',
            field=models.TimeField(auto_now=True),
        ),
    ]
