# Generated by Django 3.0.6 on 2022-06-20 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20220620_0248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='author',
        ),
    ]
