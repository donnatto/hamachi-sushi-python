# Generated by Django 2.2.7 on 2019-11-21 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sushibar', '0003_blogpost_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='url',
            field=models.URLField(null=True),
        ),
    ]
