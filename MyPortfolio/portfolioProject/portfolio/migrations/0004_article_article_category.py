# Generated by Django 3.2.18 on 2023-04-02 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_category',
            field=models.CharField(choices=[('N/A', 'N/A'), ('HOBBY', 'Hobby'), ('FOOD', 'Food'), ('PROGRAMMING', 'Programming')], default='N/A', max_length=20),
        ),
    ]
