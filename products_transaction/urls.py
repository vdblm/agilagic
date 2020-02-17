from django.urls import path
from . import views

app_name = 'products_transaction'
urlpatterns = [
    path(r'all_products.html/', views.all_products, name='all_products'),
    path(r'single_product.html/<product_id>/', views.single_product, name='single_product')

]
