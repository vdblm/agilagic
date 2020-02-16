from django.db import models
from user_authentication.models import WebsiteSeller
# Create your models here.


class Contract(models.Model):
    contract_id = models.AutoField(primary_key=True)
    percentage = models.IntegerField()
    seller = models.ForeignKey(WebsiteSeller, on_delete=models.CASCADE, related_name='seller')
    status_choices = (
        ('P', 'در حال انتظار'),  # this status is when the product is proposed but not accepted by admin
        ('S', 'تایید شده'),  # this status is when the admin accepts the product
        ('U', 'رد شده'),  # this status is when the admin denies the product
    )
    description = models.TextField(default=1)
    status = models.CharField(max_length=2, choices=status_choices)
    objects = models.Manager()

