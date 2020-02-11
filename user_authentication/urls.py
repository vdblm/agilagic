from django.urls import path
from . import views

urlpatterns = [
    path(r'customer_sign_up.html/', views.sign_up_customer, name='customer_sign_up'),
    path(r'seller_sign_up.html/', views.sign_up_seller, name='seller_sign_up'),
    # Todo forget password page
    path(r'forget_password', views.sign_up_customer, name='forget_password'),
    path(r'sign_in.html/', views.sign_in, name='sign_in'),
    path(r'sign_out.html/', views.sign_out, name='sign_out'),
]
