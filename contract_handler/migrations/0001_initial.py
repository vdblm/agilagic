# Generated by Django 3.0.3 on 2020-02-17 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('contract_id', models.AutoField(primary_key=True, serialize=False)),
                ('percentage', models.IntegerField()),
                ('description', models.TextField(default=1)),
                ('status', models.CharField(choices=[('P', 'در حال انتظار'), ('S', 'تایید شده'), ('U', 'رد شده')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='ContractManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
