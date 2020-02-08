from django.shortcuts import render
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from .models import UserManager, ContractManager, ProductManager
from .forms import SignUpForm, SignInForm, ProposeContract, ProposeProduct, ChargeAccount
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse


def seller_check(user):
    if user.is_anonymous:
        return False
    if user.is_superuser:
        return False
    my_user = UserManager.get_user_by_username(user.username)
    return my_user.is_seller


def admin_check(user):
    my_user = UserManager.get_user_by_username(user.username)
    return my_user.is_admin


@csrf_exempt
def home(request):  # this shows the home page of the website
    return render(request, 'web/index.html')


@csrf_exempt
def sign_up(request):  # the sign up form is provided for the new user
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'web/pages/sign-up.html', {'form': form})
    elif request.method == 'POST':  # this should get the input data from sign up form and add the new user to database
        # TODO: based on different results, the user have to be directed to different web pages
        # return render(request, 'web/pages/seller-profile.html')
        username, password, is_seller, name, family_name = request.POST['email'], request.POST['password'], False \
            , request.POST['name'], request.POST['family_name']
        # return render(request, 'web/pages/seller-profile.html')
        if 'type' in request.POST.keys():  # if type exists it means that the user wants to sign up as a Seller
            is_seller = True
        result = UserManager.sign_up_user(username, password, is_seller, name, family_name)
        # HttpResponse("<html><body>user email is %s.</body></html>", username)
        return render(request, 'web/pages/seller-profile.html')


@csrf_exempt
def sign_in(request):  # the login form is provided for the user
    if request.method == 'POST':
        email, password = request.POST['email'], request.POST['password']
        result = UserManager.login(request, email, password)
        if result == 'Successful Login':  # the user existed in the database with the same password as declared
            return render(request, 'web/pages/blank-page.html')
        elif result == 'no such a user':  # the declared username is not created
            return HttpResponse('This username is not defined')
        elif result == 'Wrong Password':  # the declared password is incorrect
            return HttpResponse('password problem')
    elif request.method == 'GET':
        form = SignInForm()
        return render(request, 'web/pages/login.html', {'form': form})


@csrf_exempt
@login_required(login_url='sign_in')
@user_passes_test(seller_check)
def propose_contract(request):  # the propose form is provided for the seller
    form = ProposeContract()
    return render(request, 'web/propose_contract_test.html', {'form': form})


@csrf_exempt
def propose_contract_do(request):  # the proposed contract should be saved in the database and sent to admin
    # TODO: at the end the user should be redirected to a proper web page
    percentage, description = request.POST['percentage'], request.POST['description']
    seller = UserManager.get_user_by_username(request.user.username)
    ContractManager.make_new_contract(seller=seller, profit_perc=percentage, description=description)
    return HttpResponse('We are in Propose.Do')


def sign_contract(request):
    if request.method == 'GET':
        pass


def show_contracts(request):
    if request.method == 'GET':
        pending_contracts = ContractManager.get_pending_contracts()
        response = {}
        for contract in pending_contracts:
            # TODO is_signed is boolean!!
            response[contract.id] = {'status': 'Pending', 'profit': contract.profit_perc,
                                     'seller': contract.seller.username}
        return JsonResponse(response)


@csrf_exempt
@login_required(login_url='sign_in')
@user_passes_test(seller_check)
def propose_product(request):  # this view handles the product form viewing and submitting
    if request.method == 'POST':  # the user has submitted the form
        name, price, description, img = request.POST['name'], request.POST['price'], \
                                        request.POST['description'], request.POST['img']
        owner = UserManager.get_user_by_username(request.user.username)
        ProductManager.make_new_product(name, description, owner, price, img)
        return HttpResponse('You product is added to database')
    elif request.method == 'GET':  # th user wants the form to be viewed
        form = ProposeProduct()
        return render(request, 'web/propose_product_test.html', {'form': form})


@csrf_exempt
@login_required(login_url='sign_in')
def charge_account(request):  # this view handles the account_charging form viewing and submitting the request
    if request.method == 'POST':  # the user has submitted the form
        amount, username = request.POST['amount'], request.user.username
        result = UserManager.charge_credit(username, amount)
        return HttpResponse(result)
    elif request.method == 'GET':  # the user wants th form to be viewed
        form = ChargeAccount()
        return render(request, 'web/charge_account_test.html', {'form': form})


@csrf_exempt
@login_required(login_url='sign_in')
def sign_out(request):
    UserManager.logout(request)
    return HttpResponse('You signed out successfully')
