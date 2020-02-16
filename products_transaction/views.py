from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import ProposeProduct
from .models import ProductManager, ProductBasketManager, ProductBasket
from user_authentication.models import UserManager
from user_authentication.views import user_profile
from django.core import serializers


# Create your views here.


# have to be signed_in
# the user_type should be seller
@csrf_exempt
@login_required(login_url='sign_in')
def propose_product(request):
    if request.method == 'GET':  # the form for getting product details should be shown to the seller
        return user_profile(request)
    elif request.method == 'POST':  # the details is gotten and a product object should be added to database
        form = ProposeProduct(request.POST, request.FILES)
        if form.is_valid():
            product_manager = ProductManager()
            result = product_manager.add_product(form.cleaned_data, request)
            # TODO: the database should add the product to database
        return render(request, 'web/seller-profile.html', {'new_product_form': form})


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


# the customer do not have permission for this view
@login_required(login_url='sign_in')
# TODO no need to it. it will be handled in user profile
def proposed_products(request):  # if user is admin then the products that are proposed but not accepted should be shown
    # if the user is seller the products that are not accepted should be shown
    user_manager = UserManager()
    if user_manager.check_existence(request.user.username):
        if user_manager.is_seller(request.user.username):  # the user is seller
            products = ProductManager.get_proposed_products_of_seller(request.user.username)
            qs_json = serializers.serialize('json', products)
            return HttpResponse(qs_json, content_type='application/json')
        elif user_manager.get_user_by_username(request.user.username).is_admin():  # the user is admin
            products = ProductManager.get_all_pending_products(request.user.username)
            qs_json = serializers.serialize('json', products)
            return HttpResponse(qs_json, content_type='application/json')
        else:  # the user is customer and should't be here:)
            # TODO goes to the user profile. may add some message
            return user_profile(request)
    else:
        return HttpResponse('The user does not exist')


# TODO should be only the admin
def accept_reject_product(request):
    # we may have different requests
    # request_type = 'accept' or 'reject'
    # product_id = 'product_id'
    # should make the status as 'U' (unassigned)
    res = str(request.POST['request_type']) + str(request.POST['product_id'])
    return HttpResponse(res)
