from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CustomerManager


@csrf_exempt
def sign_up(request):
    # TODO : the password field should be sent coded
    params = request.POST
    result = CustomerManager.sign_up_customer(params['username'], params['email'], params['password'])
    return HttpResponse(result)
