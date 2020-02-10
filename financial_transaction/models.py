from django.db import models
from user_authentication.models import WebsiteUser
# Create your models here.


class Transaction(models.Model):
    transaction_types = (
        ('C', 'Charge Account'),
        ('B', 'Buy Product'),
        ('U', 'Unsigned'),
        ('H', 'Hidden'),
    )
    payer = models.ForeignKey(WebsiteUser, on_delete=models.CASCADE, default='default', related_name='payer')
    receiver = models.ForeignKey(WebsiteUser, on_delete=models.CASCADE, default='default', related_name='payee')
    transaction_type = models.CharField(max_length=2, choices=transaction_types, default='B')
    amount = models.BigIntegerField(default=0)
    objects = models.Manager()