import sys

from django.db import models
from user_authentication.models import WebsiteSeller, UserManager, WebsiteCustomer


# Create your models here.


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.TextField()
    available_number = models.IntegerField()
    seller = models.ForeignKey(WebsiteSeller, on_delete=models.CASCADE, related_name='seller')
    status_choices = (
        ('P', 'Pending'),  # this status is when the product is proposed but not accepted by admin
        ('S', 'Signed'),  # this status is when the admin accepts the product
        ('U', 'Unsigned'),  # this status is when the admin denies the product
        ('H', 'Hidden'),  # this status is when the charge of the seller is less than a pre-defined threshold
    )
    description = models.TextField(default=1)
    status = models.CharField(max_length=2, choices=status_choices)
    price = models.BigIntegerField(default=0)
    img = models.ImageField(null=True, upload_to='images/')
    objects = models.Manager()


class ProductBasket(models.Model):
    owner = models.ForeignKey(WebsiteCustomer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    objects = models.Manager()

    # TODO : a list of products

    def buy(self):  # available number of products should be decreased
        # the address should be selected
        pass

    def add_product(self, product):  # this method gets a product and adds it to the list of products
        pass


class ProductManager(models.Manager):

    @staticmethod
    def add_product(details_dictionary, request):  # this method adds a new proposed product to the database
        name = details_dictionary['name']
        available_number = details_dictionary['available_number']
        description = details_dictionary['description']
        price = details_dictionary['price']
        image = details_dictionary['image']
        user_manager = UserManager()
        user = user_manager.get_seller_by_username(request.user.username)
        product = Product(name=name, available_number=available_number, seller=user, status='P',
                          description=description, price=price, img=image)
        product.save()
        return 'the product was successfully added to the database'

    @staticmethod
    def get_product(product_id):  # this method returns the product by getting the product id
        return Product.objects.get(product_id=product_id)

    @staticmethod
    def get_products_list():  # this method gives all products that can be shown on the list for customers
        return Product.objects.filter(status='S')


class ProductBasketManager(models.Manager):

    @staticmethod
    def check_existence_of_basket_for_user(username):  # this method gets a username and checks if a ProductBasket has
        # been initialized for the user
        user_manager = UserManager()
        if user_manager.is_customer(username):
            user = user_manager.get_customer_by_username(username)
            return ProductBasket.objects.filter(owner=user).exists()
        else:
            return False

    @staticmethod
    def get_basket_for_user(username):  # this method gives the basket of a user
        user_manager = UserManager()
        user = user_manager.get_customer_by_username(username)
        return ProductBasket.objects.get(owner=user)[0]

    @staticmethod
    def add_basket(username):  # this method initializes a basket for the user given his username
        user_manager = UserManager()
        user = user_manager.get_customer_by_username(username)
        basket = ProductBasket(owner=user)
        return basket
