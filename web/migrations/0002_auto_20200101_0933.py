# Generated by Django 3.0 on 2020-01-01 09:33

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customer',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]