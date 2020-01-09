from django.urls import path
from . import views

urlpatterns = [
    path(r'home/', views.home, name='home'),
    path(r'home/sign_up.html/', views.sign_up, name='sign_up'),
    path(r'home/sign_in.html/', views.sign_in, name='sign_in'),
    path(r'home/sign_in_do.html/', views.sign_in_do, name='sign_in_do'),
    path(r'home/sign_up_do.html/', views.sign_up_do, name='sign_up_do'),

]
