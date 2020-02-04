from django.urls import path
from . import views

urlpatterns = [
    path(r'home/', views.home, name='home'),
    path(r'sign_up.html/', views.sign_up, name='sign_up'),
    path(r'sign_in.html/', views.sign_in, name='sign_in'),
    path(r'sign_up_do.html/', views.sign_up_do, name='sign_up_do'),
    path(r'propose_contract.html/', views.propose_contract, name='propose_contract'),
    path(r'propose_contract_do.html/', views.propose_contract_do, name='propose_contract_do'),
    path(r'show_contracts/', views.show_contracts, name='show_contracts'),
]
