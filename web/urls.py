from django.urls import path
from . import views

urlpatterns = [
    path(r'home/', views.home, name='home'),
    path(r'sign_up.html/', views.sign_up, name='sign_up'),
    path(r'sign_in.html/', views.sign_in, name='sign_in'),
    path(r'propose_contract.html/', views.propose_contract, name='propose_contract'),
    path(r'propose_contract_do.html/', views.propose_contract_do, name='propose_contract_do'),
    path(r'show_contracts/', views.show_contracts, name='show_contracts'),
    path(r'propose_product.html/', views.propose_product, name='propose_product'),
    path(r'charge_account.html/', views.charge_account, name='charge_account'),
    path(r'sign_out.html/', views.sign_out, name='sign_out'),
]
