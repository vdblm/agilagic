from django.db import models
from user_authentication.models import WebsiteUser
# Create your models here.


class Transaction(models.Model):
    transaction_types = (
        ('C', 'Charge Account'),
        ('B', 'Buy Product'),
        ('D', 'Divide'),
    )
    payer = models.ForeignKey(WebsiteUser, on_delete=models.CASCADE, default=1, related_name='payer')
    receiver = models.ForeignKey(WebsiteUser, on_delete=models.CASCADE, default=1, related_name='payee')
    transaction_type = models.CharField(max_length=2, choices=transaction_types, default=1)
    amount = models.BigIntegerField(default=0)
    objects = models.Manager()