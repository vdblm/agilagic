from django.contrib.auth import authenticate, login
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class UserManager(models.Manager):
    @staticmethod
    def sign_up_user(username, password, is_seller, name, family_name):
        # this methods adds a user to the database if the username is not taken
        exists = UserManager.check_existence(username)
        if not exists:
            WebsiteUser.objects.create_user(username=username, email=username, password=password, is_seller=is_seller,
                                            is_admin=False, credit=0, first_name=name, last_name=family_name)
            return 'Sign up completed successfully'
        else:
            return 'The username is used'

    @staticmethod
    def check_existence(username):
        # this method checks if the username exists in the database
        return User.objects.filter(username=username).exists()

    @staticmethod
    def login(request, username, password):
        # this method checks if the username exists. In the condition of existence if checks the password.
        if not UserManager.check_existence(username):
            return 'no such a user'
        else:
            user = authenticate(username=username, password=password)
            if user is None:
                return 'Wrong Password'
            login(request=request, user=user)
            return 'Successful Login'

    @staticmethod
    def get_user_by_username(username):
        return WebsiteUser.objects.get(username=username)


class WebsiteUser(User):
    is_seller = models.BooleanField()
    is_admin = models.BooleanField()
    credit = models.BigIntegerField()


class Product(models.Model):
    pass


class Contract(models.Model):
    status_choices = (
        ('P', 'Pending'),
        ('S', 'Signed'),
        ('U', 'Unsigned'),
    )
    seller = models.ForeignKey(WebsiteUser, on_delete=models.CASCADE)
    description = models.TextField()
    response = models.TextField()
    is_signed = models.CharField(max_length=2, choices=status_choices)
    profit_perc = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    objects = models.Manager()

    def sign_contract(self, sign, response):
        self.is_signed = sign
        self.response = response

    def propose_contract(self, seller, description, profit_perc):
        self.seller = seller
        self.description = description
        self.profit_perc = profit_perc

    def __unicode__(self):
        return self.seller.first_name + " " + self.seller.last_name


class ContractManager(models.Manager):
    @staticmethod
    def get_pending_contracts():
        return Contract.objects.filter(is_signed='P')

    @staticmethod
    def make_new_contract(seller, description, profit_perc, response='', is_signed='P'):
        contract = Contract(seller=seller, description=description, response=response, profit_perc=profit_perc,
                            is_signed=is_signed)
        contract.save()
