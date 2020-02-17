from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

from contract_handler.models import Contract, ContractManager
from products_transaction.models import ProductManager
from .models import UserManager, WebsiteSeller
from .forms import SignInForm, CustomerSignUpForm, SellerSignUpForm
from django.contrib.auth.decorators import login_required, user_passes_test

import products_transaction.forms as product_forms
from products_transaction.views import all_products
import products_transaction.models as product_models
import contract_handler.forms as contract_forms


@csrf_exempt
def sign_up_customer(request):
    messages = []
    if request.method == 'GET':
        form = CustomerSignUpForm()
    else:
        form = CustomerSignUpForm(request.POST)
        user_manager = UserManager()
        if form.is_valid():
            result = user_manager.sign_up_user(is_customer=True, data=form.cleaned_data)
            if result == 'Sign up completed successfully':
                # TODO go to the customer profile page
                username = form.cleaned_data['email']
                password = form.cleaned_data['password']
                UserManager.login(request, username, password)
                return user_profile(request)
            else:
                messages.append('ایمیل وارد شده تکراری است')

    return render(request, 'web/pages/sign-up.html', {'form': form, 'messages': messages})


@csrf_exempt
def sign_up_seller(request):
    messages = []
    if request.method == 'GET':
        form = SellerSignUpForm()
    else:
        form = SellerSignUpForm(request.POST)
        user_manager = UserManager()
        if form.is_valid():
            result = user_manager.sign_up_user(is_customer=False, data=form.cleaned_data)
            if result == 'Sign up completed successfully':
                # TODO go to the seller profile page
                username = form.cleaned_data['email']
                password = form.cleaned_data['password']
                UserManager.login(request, username, password)
                return user_profile(request)
            else:
                messages.append('ایمیل وارد شده تکراری است')
        else:
            return HttpResponse('the form is not valid')

    return render(request, 'web/pages/sign-up.html', {'form': form, 'messages': messages})


@csrf_exempt
def sign_in(request):  # the login form is provided for the user
    form = None
    messages = []
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email, password = form.cleaned_data['email'], form.cleaned_data['password']
            result = UserManager.login(request, email, password)
            if result == 'Successful Login':  # the user existed in the database with the same password as declared
                # TODO go to profile
                UserManager.login(request, email, password)
                return user_profile(request)
            elif result == 'no such a user':  # the declared username is not created
                message = 'کاربری با ایمیل وارد‌شده وجود ندارد'
                messages.append(message)
            elif result == 'Wrong Password':  # the declared password is incorrect
                message = 'رمز عبور اشتباه است'
                messages.append(message)
    elif request.method == 'GET':
        form = SignInForm()

    return render(request, 'web/pages/login.html', {'form': form, 'messages': messages})


@csrf_exempt
@login_required(login_url='sign_in')
def sign_out(request):
    UserManager.logout(request)
    return redirect(all_products)


@csrf_exempt
@login_required(login_url='sign_in')
def user_profile(request):
    # TODO forms should be made
    username = request.user.username
    # check the user exists
    if UserManager.check_existence(username):
        user = UserManager.get_user_by_username(username)
        if user.is_admin():
            products = ProductManager.get_all_pending_products(user.username)
            contracts = ContractManager.get_all_pending_contracts(user.username)
            if request.method == 'POST':
                admin_profile(request)
            return render(request, 'web/admin-profile.html', {'products': products,
                                                              'user': user,
                                                              'contracts': contracts})
        elif UserManager.is_seller(user):
            # seller forms
            if request.method == 'POST':
                seller_profile(request)
            products = ProductManager.get_proposed_products_of_seller(user.username)
            new_product_form = product_forms.ProposeProduct()
            new_contract_form = contract_forms.ProposeContract()
            contract = None
            if Contract.objects.filter(contract_seller=user).exists():
                new_contract_form = None
                contract = Contract.objects.get(contract_seller=user)
            return render(request, 'web/seller-profile.html', {'new_product_form': new_product_form,
                                                               'new_contract_form': new_contract_form,
                                                               'products': products,
                                                               'user': user,
                                                               'contract': contract})
        else:
            basket = product_models.ProductBasketManager.get_basket_for_user(user)
            basket_products = basket.products.all()
            return render(request, 'web/user-profile.html', {'user': user,
                                                             'basket_products': basket_products})
    else:
        # TODO what should we do?:)
        return HttpResponse('the user does not exists')


def seller_profile(request):
    # Handle propose contract
    if 'propose-product' in request.POST:

        form = product_forms.ProposeProduct(request.POST, request.FILES)
        if form.is_valid():
            product_manager = ProductManager()
            result = product_manager.add_product(form.cleaned_data, request)
            # TODO: the database should add the product to database
    elif 'propose-contract' in request.POST:
        propose_contract = contract_forms.ProposeContract(request.POST)
        if propose_contract.is_valid():
            description = propose_contract.cleaned_data['description']
            percentage = propose_contract.cleaned_data['percentage']
            seller = UserManager.get_seller_by_username(request.user.username)
            contract = Contract(description=description, percentage=percentage, status='P', contract_seller=seller)
            contract.save()


def admin_profile(request):
    if 'accept-product' in request.POST or 'reject-product' in request.POST:
        product_id = request.POST['product_id']
        product = ProductManager.get_product(product_id)
        if 'accept-product' in request.POST:
            product.status = 'S'
        else:
            product.status = 'U'
        product.save()
    elif 'accept-contract' in request.POST or 'reject-contract' in request.POST:
        contract_id = request.POST['contract_id']
        contract = ContractManager.get_contract(contract_id)
        if 'accept-contract' in request.POST:
            contract.status = 'S'
        else:
            contract.status = 'U'
        contract.save()


def error404_view(request, exception):
    return render(request, 'web/pages/404-page.html')
