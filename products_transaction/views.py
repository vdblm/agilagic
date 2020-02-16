from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import ProposeProduct
from .models import ProductManager, ProductBasketManager, ProductBasket
from user_authentication.models import UserManager
from django.core import serializers


# Create your views here.

def all_products(request):
    if request.method == 'GET':  # a query should be sent to the database and all products should be returned
        products = ProductManager.get_products_list()
        if UserManager.check_existence(request.user.username):
            user = UserManager.get_user_by_username(request.user.username)
        else:
            user = None
        return render(request, 'web/products-list.html', {'products': products, 'user': user})
    elif request.method == 'POST':
        if request.POST['request_type'] == 'add_to_basket':  # the product ID is gotten and it should be added to the
            # Basket
            # it should be checked if a ProductBasket is initialized for the user
            basket_manager = ProductBasketManager()
            product_id = request.POST['product_id']
            if basket_manager.check_existence_of_basket_for_user(request.user.username):  # now find the basket and add
                # the product to basket
                product_basket = basket_manager.get_basket_for_user(request.user.username)
            else:  # first a basket should be initialized then the product should be added to the basket
                product_basket = basket_manager.add_basket(request.user.username)
            product = ProductManager.get_product(product_id)
            product_basket.add_product(product)
            return HttpResponse('the product is added to the basket')

        else:  # this is for other potential requests of this url
            pass


# TODO should be only the admin
def accept_reject_product(request):
    # we may have different requests
    # request_type = 'accept' or 'reject'
    # product_id = 'product_id'
    # should make the status as 'U' (unassigned)
    if request.method == 'POST':
        request_type = request.POST['request_type']
        product_id = request.POST['product_id']
        product = ProductManager.get_product(product_id)
        if request_type == 'accept':
            product.status = 'S'
        elif request_type == 'reject':
            product.status = 'U'
        product.save()
    res = str(request.POST['request_type']) + str(request.POST['product_id'])
    return HttpResponse(res)
