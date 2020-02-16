from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import ProposeProduct
from .models import ProductManager, ProductBasketManager, ProductBasket
from user_authentication.models import UserManager
from user_authentication.views import user_profile
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
