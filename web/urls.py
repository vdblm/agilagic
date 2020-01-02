from django.urls import path
from . import views

urlpatterns = [
    path(r'sign_up/customer/', views.sign_up, name='sign_up_customer')
]
