from django.urls import path
from . import views

urlpatterns = [
    path(r'home/', views.home, name='home'),
    path(r'home/sign_up.html/', views.sign_up, name='sign_up'),
    path(r'home/sign_in.html/', views.sign_in, name='sign_in')
]
