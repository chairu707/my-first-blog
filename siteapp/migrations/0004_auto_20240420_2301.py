# Generated by Django 3.1.2 on 2024-04-20 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0003_auto_20240414_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
