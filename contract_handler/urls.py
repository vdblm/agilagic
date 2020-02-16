from django.urls import path
from . import views

app_name = 'products_transaction'
urlpatterns = [
    path(r'propose_contract.html/', views.propose_contract, name='propose_contract'),

]
