from django.urls import path
from . import views

urlpatterns = [
    path(r'charge_account.html/', views.charge_account, name='charge_account'),
    path(r'pay.html/<int:amount>/<slug:transaction_type>/', views.pay, name='pay'),

]
