from django.http import HttpResponse
from django.shortcuts import render
from .forms import ProposeProduct
from .models import ProductManager
# Create your views here.


# have to be signed_in
# the user_type should be seller
def propose_product(request):
    if request.method == 'GET':  # the form for getting product details should be shown to the seller
        form = ProposeProduct()
        return render(request, 'financial_transaction/form_viewer.html', {'form': form})
    elif request.method == 'POST':  # the details is gotten and a product object should be added to database
        form = ProposeProduct(request.POST)
        if form.is_valid():
            product_manager = ProductManager()
            product_manager.add_product(form.cleaned_data, request)
            # TODO: the database should add the product to database
        else:
            HttpResponse('Form inputs are not valid')
