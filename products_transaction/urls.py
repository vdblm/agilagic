from django.urls import path
from . import views

urlpatterns = [
    path(r'propose_product.html/', views.propose_product, name='propose_product'),
    path(r'all_products.html/', views.all_products, name='all_products'),

]