# Generated by Django 3.1.2 on 2021-03-13 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='youtube',
        ),
    ]
