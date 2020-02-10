from django.shortcuts import render
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from .models import UserManager
from .forms import SignInForm, CustomerSignUpForm, SellerSignUpForm
from django.contrib.auth.decorators import login_required, user_passes_test


@csrf_exempt
def sign_up(request):  # the sign up form is provided for the new user
    if request.method == 'GET':
        form = CustomerSignUpForm()
        if request.path == '/seller_sign_up.html/':
            form = SellerSignUpForm('seller')
        return render(request, 'web/pages/sign-up.html', {'form': form})
    elif request.method == 'POST':  # this should get the input data from sign up form and add the new user to database
        form, is_customer = None, True
        user_manager = UserManager()
        if request.path == '/customer_sign_up.html/':
            form, is_customer = CustomerSignUpForm(request.POST), True  # email, password, name, family_name
        elif request.path == '/seller_sign_up.html/':
            form, is_customer = SellerSignUpForm(request.POST), False  # email, password, name, number
        if form.is_valid():
            result = user_manager.sign_up_user(is_customer, form.cleaned_data)
        else:
            result = 'the form is not valid'
        my_print(result)

        '''
        # return render(request, 'web/pages/seller-profile.html')
        username, password, is_seller, name, family_name = request.POST['email'], request.POST['password'], False \
            , request.POST['name'], request.POST['family_name']
        # return render(request, 'web/pages/seller-profile.html')
        if 'type' in request.POST.keys():  # if type exists it means that the user wants to sign up as a Seller
            is_seller = True
        result = UserManager.sign_up_user(username, password, is_seller, name, family_name)
        # HttpResponse("<html><body>user email is %s.</body></html>", username)
        return render(request, 'web/pages/seller-profile.html')
        '''


@csrf_exempt
def sign_in(request):  # the login form is provided for the user
    if request.method == 'POST':
        form = SignInForm(request.POST)
        my_print(request.POST)
        if form.is_valid():
            email, password = form.cleaned_data['email'], form.cleaned_data['password']
            result = UserManager.login(request, email, password)
            if result == 'Successful Login':  # the user existed in the database with the same password as declared
                return render(request, 'web/pages/blank-page.html')
            elif result == 'no such a user':  # the declared username is not created
                return HttpResponse('This username is not defined')
            elif result == 'Wrong Password':  # the declared password is incorrect
                return HttpResponse('password problem')
        else:
            return HttpResponse('form is not valid')
    elif request.method == 'GET':
        form = SignInForm()
        return render(request, 'web/pages/login.html', {'form': form})


@csrf_exempt
@login_required(login_url='sign_in')
def sign_out(request):
    UserManager.logout(request)
    return HttpResponse('You signed out successfully')


def my_print(text):
    print('################################################################################')
    print(text)
    print('################################################################################')