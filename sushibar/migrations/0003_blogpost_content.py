# Generated by Django 2.2.7 on 2019-11-21 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sushibar', '0002_blogpost_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
