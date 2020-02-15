from django.shortcuts import render
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from .models import UserManager, WebsiteSeller
from .forms import SignInForm, CustomerSignUpForm, SellerSignUpForm
from django.contrib.auth.decorators import login_required, user_passes_test


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
                return render(request, 'web/pages/')
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
                user = UserManager.get_user_by_username(username)
                return render(request, 'web/pages/seller-profile.html', {'user': user})
            else:
                messages.append('ایمیل وارد شده تکراری است')

    return render(request, 'web/pages/sign-up.html', {'form': form, 'messages': messages})


@csrf_exempt
def sign_in(request):  # the login form is provided for the user
    form = None
    messages = []
    if request.method == 'POST':
        form = SignInForm(request.POST)
        my_print(request.POST)
        if form.is_valid():
            email, password = form.cleaned_data['email'], form.cleaned_data['password']
            result = UserManager.login(request, email, password)
            if result == 'Successful Login':  # the user existed in the database with the same password as declared
                # TODO go to profile
                return render(request, 'web/pages/blank-page.html')
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
    return HttpResponse('You signed out successfully')


@csrf_exempt
@login_required(login_url='sign_in')
def user_profile(request, username):
    user = UserManager.get_user_by_username(username)
    my_print(type(user))
    if isinstance(user, WebsiteSeller):
        return render(request, 'web/pages/seller-profile.html', {'user': user})
    else:
        # TODO customer page
        pass


def my_print(text):
    print('################################################################################')
    print(text)
    print('################################################################################')
