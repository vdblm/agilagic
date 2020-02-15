from django.db import models
from user_authentication.models import WebsiteSeller, WebsiteCustomer


# Create your models here.


class Product(models.Model):
    name = models.TextField()
    available_number = models.IntegerField()
    seller = models.ForeignKey(WebsiteSeller, on_delete=models.CASCADE, related_name='seller')
    status_choices = (
        ('P', 'Pending'),  # this status is when the product is proposed but not accepted by admin
        ('S', 'Signed'),  # this status is when the admin accepts the product
        ('U', 'Unsigned'),  # this status is when the admin denies the product
        ('H', 'Hidden'),  # this status is when the charge of the seller is less than a pre-defined threshold
    )
    description = models.TextField(default='default')
    status = models.CharField(max_length=2, choices=status_choices)
    price = models.BigIntegerField(default=0)
    # img = models.ImageField(null=True)
    objects = models.Manager()

    def add_to_basket(self):
        pass


class ProductBasket(models.Model):
    owner = models.ForeignKey(WebsiteCustomer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    # TODO : a list of products

    def buy(self):  # available number of products should be decreased
        # the address should be selected
        pass


class ProductManager(models.Manager):

    def add_product(self, details_dictionary, request):  # this method adds a new proposed product to the database
        try:
            name = details_dictionary['name']
            available_number = details_dictionary['available_number']
            description = details_dictionary['description']
            price = details_dictionary['price']
            product = Product(name=name, available_number=available_number, seller=request.user, status='P',
                              description=description, price=price)
            product.save()
        except:
            print('##########################################################')
            print('something bad happened while adding product to database')
            print('##########################################################')
