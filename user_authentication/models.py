from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


class WebsiteUser(User):
    # is_admin = models.BooleanField()
    credit = models.BigIntegerField(default=0)

    def is_admin(self):
        return self.is_staff


class WebsiteCustomer(WebsiteUser):
    # TODO complete it!
    deliver_address = models.TextField()


class WebsiteSeller(WebsiteUser):
    company_number = models.BigIntegerField(default=000000)
    company_name = models.CharField(max_length=20, default=0)


class UserManager(models.Manager):
    @staticmethod
    def sign_up_user(is_customer, data):
        # this methods adds a user to the database if the username is not taken
        exists = UserManager.check_existence(data['email'])
        if not exists:
            if is_customer:
                WebsiteCustomer.objects.create_user(username=data['email'], email=data['email'],
                                                    password=data['password'],
                                                    credit=0, first_name=data['name'], last_name=data['family_name'])
            else:
                WebsiteSeller.objects.create_user(username=data['email'], email=data['email'],
                                                  password=data['password'],
                                                  credit=0, company_name=data['name'],
                                                  company_number=data['number'])
            return 'Sign up completed successfully'
        else:
            return 'The username is used'

    @staticmethod
    def check_existence(username):
        # this method checks if the username exists in the database
        return WebsiteUser.objects.filter(username=username).exists()

    @staticmethod
    def login(request, username, password):
        # this method checks if the username exists. In the condition of existence it checks the password.
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

    @staticmethod
    def get_seller_by_username(username):
        return WebsiteSeller.objects.get(username=username)

    @staticmethod
    def get_customer_by_username(username):
        return WebsiteCustomer.objects.get(username=username)

    @staticmethod
    def is_customer(username):
        return WebsiteCustomer.objects.filter(username=username).exists()

    @staticmethod
    def is_seller(username):
        return WebsiteSeller.objects.filter(username=username).exists()

    @staticmethod
    def charge_credit(username, amount):
        user = UserManager.get_user_by_username(username)
        user.credit += int(amount)
        user.save()
        return 'Your request is done. Your current charge is: ' + str(user.credit)

    @staticmethod
    def logout(request):
        logout(request)
