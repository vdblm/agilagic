from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import SignUpForm, SignInForm
from django.contrib.auth import views as auth_views

from django.views.decorators.csrf import csrf_exempt
from .models import *
from .models import UserManager, ContractManager
from .forms import SignUpForm, SignInForm, ProposeContract
from django.shortcuts import redirect


@csrf_exempt
def home(request):  # this shows the home page of the website
    return render(request, 'web/index.html')


@csrf_exempt
def sign_up(request):  # the sign up form is provided for the new user
    form = SignUpForm()
    return render(request, 'web/SignUp_test.html', {'form': form})


@csrf_exempt
def sign_up_do(request):  # this should get the input data from sign up form and add the new user to database
    # TODO: based on different results, the user have to be directed to different web pages
    username, password, is_seller = request.POST['email'], request.POST['password'], False
    if 'type' in request.POST.keys():  # if type exists it means that the user wants to sign up as a Seller
        is_seller = True
    result = UserManager.sign_up_user(username, password, is_seller)
    return HttpResponse(result)


@csrf_exempt
def sign_in(request):  # the login form is provided for the user
    form = SignInForm()
    return render(request, 'web/SignIn_test.html', {'form': form})


@csrf_exempt
def sign_in_do(request):  # check email and password if it exists in the database
    email, password = request.POST['email'], request.POST['password']
    result = UserManager.login(request, email, password)
    if result == 'Successful Login':  # the user existed in the database with the same password as declared
        return render(request, 'web/index.html')
    elif result == 'no such a user':  # the declared username is not created
        return HttpResponse('This username is not defined')
    elif result == 'Wrong Password':  # the declared password is incorrect
        return HttpResponse('password problem')
    else:
        return HttpResponse('WTF')


@csrf_exempt
def propose_contract(request):  # the propose form is provided for the seller
    if not request.user.is_authenticated:  # if the user is not logged in he should be redirected to login page
        return redirect('sign_in')
    user = UserManager.get_user_by_username(request.user.username)
    if not user.is_seller:  # if the user is logged in but not as a seller, he must not have permission to make contract
        return HttpResponse('You are not a seller')
    form = ProposeContract()
    return render(request, 'web/propose_contract_test.html', {'form': form})


@csrf_exempt
def propose_contract_do(request):  # the proposed contract should be saved in the database and sent to admin
    # TODO: at the end the user should be redirected to a proper web page
    percentage, description = request.POST['percentage'], request.POST['description']
    seller = UserManager.get_user_by_username(request.user.username)
    ContractManager.make_new_contract(seller=seller, profit_perc=percentage, description=description)
    return HttpResponse('We are in Propose.Do')
