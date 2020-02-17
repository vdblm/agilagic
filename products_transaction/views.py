from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .forms import ProposeProduct
from .models import ProductManager, ProductBasketManager, ProductBasket
from user_authentication.models import UserManager
from django.core import serializers


# Create your views here.

def all_products(request):
    # a query should be sent to the database and all products should be returned
    products = ProductManager.get_products_list()
    if UserManager.check_existence(request.user.username):
        user = UserManager.get_user_by_username(request.user.username)
    else:
        user = None
    messages = []
    if request.method == 'POST':
        if request.POST['request_type'] == 'add_to_basket':  # the product ID is gotten and it should be added to the
            # Basket
            # it should be checked if a ProductBasket is initialized for the user
            basket_manager = ProductBasketManager()
            if user is None:
                messages.append('لطفا ابتدا وارد شوید')
            elif not UserManager.is_customer(user.username):
                messages.append('شما مشتری نیستید')
            else:
                user = UserManager.get_customer_by_username(user.username)
                product_id = request.POST['product_id']

                if basket_manager.check_existence_of_basket_for_user(user):  # now find the basket and add
                    # the product to basket
                    product_basket = basket_manager.get_basket_for_user(user)
                else:  # first a basket should be initialized then the product should be added to the basket
                    product_basket = basket_manager.add_basket(user)
                product = ProductManager.get_product(product_id)
                if product_basket.products.filter(product_id=product.product_id).exists():
                    messages.append('کالا در سبد خریدتان موجود است')
                else:
                    product_basket.add_product(product)
                    messages.append('کالا به سبد خریدتان اضافه شد')

        else:  # this is for other potential requests of this url
            pass
    return render(request, 'web/products-list.html', {'products': products, 'user': user,
                                                      'messages': messages})


def single_product(request, product_id):
    # a query should be sent to the database and all products should be returned
    product = ProductManager.get_product(product_id)
    if UserManager.check_existence(request.user.username):
        user = UserManager.get_user_by_username(request.user.username)
    else:
        user = None
    messages = []
    if request.method == 'POST':
        if request.POST['request_type'] == 'add_to_basket':  # the product ID is gotten and it should be added to the
            # Basket
            # it should be checked if a ProductBasket is initialized for the user
            basket_manager = ProductBasketManager()
            if user is None:
                messages.append('لطفا ابتدا وارد شوید')
            elif not UserManager.is_customer(user.username):
                messages.append('شما مشتری نیستید')
            else:
                user = UserManager.get_customer_by_username(user.username)
                product_id = request.POST['product_id']

                if basket_manager.check_existence_of_basket_for_user(user):  # now find the basket and add
                    # the product to basket
                    product_basket = basket_manager.get_basket_for_user(user)
                else:  # first a basket should be initialized then the product should be added to the basket
                    product_basket = basket_manager.add_basket(user)
                product = ProductManager.get_product(product_id)
                if product_basket.products.filter(product_id=product.product_id).exists():
                    messages.append('کالا در سبد خریدتان موجود است')
                else:
                    product_basket.add_product(product)
                    messages.append('کالا به سبد خریدتان اضافه شد')

        else:  # this is for other potential requests of this url
            pass
    return render(request, 'web/single-product.html', {'product': product, 'user': user,
                                                       'messages': messages})
