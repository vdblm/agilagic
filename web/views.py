from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CustomerManager
from .forms import SignUpForm, SignInForm


@csrf_exempt
def home(request):
    # this shows the home page of the website
    return render(request, 'web/index.html')


@csrf_exempt
def sign_up(request):
    # the sign up form is provided for the new user
    return render(request, 'web/sign_up.html')


@csrf_exempt
def verify_sign_up(request):
    # this should get the input data from sign up form and add the new user to database
    params = request.POST
    result = CustomerManager.sign_up_customer(params['username'], params['email'], params['password'])
    return HttpResponse('sign up completed')


@csrf_exempt
def sign_in(request):
    # the login form is provided for the user
    form = SignInForm()
    return render(request, 'web/SignIn.html', {'form': form})


@csrf_exempt
def sign_in_do(request):
    # TODO : check email and password if it exists in the database
    email, password = request.POST['email'], request.POST['password']
    return HttpResponse(request.POST['email'])
