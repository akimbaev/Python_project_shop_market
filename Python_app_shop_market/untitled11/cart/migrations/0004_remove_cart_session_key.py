# Generated by Django 2.2.6 on 2019-12-07 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20191207_1323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='session_key',
        ),
    ]