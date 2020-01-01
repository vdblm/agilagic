from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def sign_up(request, username):
    return HttpResponse("A Customer with name: %s" % username)
