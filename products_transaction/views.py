from django.http import HttpResponse
from django.shortcuts import render
from .forms import ProposeProduct
from .models import ProductManager, ProductBasketManager, ProductBasket
from user_authentication.models import UserManager
from django.core import serializers


# Create your views here.


# have to be signed_in
# the user_type should be seller
def propose_product(request):
    if request.method == 'GET':  # the form for getting product details should be shown to the seller
        form = ProposeProduct()
        return render(request, 'financial_transaction/form_viewer.html', {'form': form})
    elif request.method == 'POST':  # the details is gotten and a product object should be added to database
        form = ProposeProduct(request.POST)
        if form.is_valid():
            product_manager = ProductManager()
            result = product_manager.add_product(form.cleaned_data, request)
            # TODO: the database should add the product to database
            return HttpResponse(result)
        else:
            return HttpResponse('Form inputs are not valid')


def all_products(request):
    if request.method == 'GET':  # a query should be sent to the database and all products should be returned
        products = ProductManager.get_products_list()
        return render(request, 'web/products-list.html', {'products': products})
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
def proposed_products(request):  # if user is admin then the products that are proposed but not accepted should be shown
    # if the user is customer the products that are not accepted should be shown
    user_manager = UserManager()
    if user_manager.is_seller(request.user.username):  # the user is seller
        products = ProductManager.get_proposed_products_of_seller(request.user.username)
        qs_json = serializers.serialize('json', products)
        return HttpResponse(qs_json, content_type='application/json')
    elif user_manager.get_user_by_username(request.user.username).is_admin():  # the user is admin
        products = ProductManager.get_all_pending_products(request.user.username)
        qs_json = serializers.serialize('json', products)
        return HttpResponse(qs_json, content_type='application/json')
    else:  # the user is customer and should't be here:)
        pass


