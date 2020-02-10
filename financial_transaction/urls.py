from django.urls import path
from . import views

urlpatterns = [
    path(r'charge_account.html/', views.charge_account, name='charge_account'),

]
