from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class CustomerManager(models.Manager):
    @staticmethod
    def sign_up_customer(username, email, password):
        # this methods adds a user to the database if the username is not taken
        exists = CustomerManager.check_existence(username)
        if not exists:
            Customer.objects.create_user(username, email, password)
            return 'Sign up completed successfully'
        else:
            return 'The username is used'

    @staticmethod
    def check_existence(username):
        # this method checks if the username exists in the database
        return Customer.objects.filter(username=username).exists()


class SellerManager(models.Manager):
    pass


class Customer(User):
    pass


class Seller(User):
    is_Admin = models.BooleanField
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
