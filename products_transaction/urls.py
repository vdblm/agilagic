from django.urls import path
from . import views

app_name = 'products_transaction'
urlpatterns = [
    path(r'propose_product.html/', views.propose_product, name='propose_product'),
    path(r'all_products.html/', views.all_products, name='all_products'),
    path(r'proposed_products.html/', views.proposed_products, name='proposed_products'),  # admin and customer can
    # check products

]
