# Generated by Django 3.0.3 on 2020-02-17 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_authentication', '0001_initial'),
        ('financial_transaction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='payer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='payer', to='user_authentication.WebsiteUser'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='receiver',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='payee', to='user_authentication.WebsiteUser'),
        ),
    ]
