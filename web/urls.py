from django.urls import path
from . import views

urlpatterns = [
    path(r'sign_up/<username>/', views.sign_up, name='sign_up')
]