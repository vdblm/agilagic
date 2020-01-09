# Generated by Django 3.0 on 2020-01-09 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='is_signed',
            field=models.CharField(choices=[('P', 'Pending'), ('S', 'Signed'), ('U', 'Unsigned')], max_length=2),
        ),
    ]
