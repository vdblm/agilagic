from django.shortcuts import render
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from .models import *


# Create your views here.

@csrf_exempt
def sign_up(request):
    name = request.POST.get('name')
    last_name = request.POST.get('last_name')

    Customer.objects.create(email='ba@g.com', last_name=last_name, username=name, first_name=name, password='sdfsq')
    return HttpResponse('OK')
