from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Admin(User):
    pass


class CustomerManager(models.Manager):
    def sign_customer(self):
        pass


class Customer(User):
    customers = models.Manager()


class Seller(User):
    credit = models.BigIntegerField()


class Product(models.Model):
    pass


class Contract(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    description = models.TextField()
    response = models.TextField()
    is_signed = models.BooleanField()
    profit_perc = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    def sign_contract(self, sign, response):
        self.is_signed = sign
        self.response = response

    def propose_contract(self, seller, description, profit_perc):
        self.seller = seller
        self.description = description
        self.profit_perc = profit_perc

    def __unicode__(self):
        return self.seller.first_name + " " + self.seller.last_name
