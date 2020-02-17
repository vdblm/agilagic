from django.db import models
from user_authentication.models import WebsiteSeller, UserManager


# Create your models here.


class Contract(models.Model):
    contract_id = models.AutoField(primary_key=True)
    percentage = models.IntegerField()
    contract_seller = models.ForeignKey(WebsiteSeller, on_delete=models.CASCADE, related_name='contract_seller')
    status_choices = (
        ('P', 'در حال انتظار'),  # this status is when the product is proposed but not accepted by admin
        ('S', 'تایید شده'),  # this status is when the admin accepts the product
        ('U', 'رد شده'),  # this status is when the admin denies the product
    )
    description = models.TextField(default=1)
    status = models.CharField(max_length=2, choices=status_choices)
    objects = models.Manager()


class ContractManager(models.Model):
    @staticmethod
    def get_all_pending_contracts(username):  # the only user who have access is admin - this method returns all of the
        # products which are pending to the admin
        user = UserManager.get_user_by_username(username)
        if user.is_admin():
            return Contract.objects.filter(status__in=['P'])
        else:  # the user is not admin and and exception have to be thrown
            return 'the user is not admin'

    @staticmethod
    def get_contract(contract_id):  # this method returns the product by getting the product id
        return Contract.objects.get(contract_id=contract_id)
