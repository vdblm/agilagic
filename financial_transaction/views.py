from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import SpecifyAmount, BankForm
# Create your views here.


# @login_required(login_url='sign_in')
@csrf_exempt
def charge_account(request):
    if request.method == 'POST':  # the user should be redirected to bank page and the amount should be pssed
        form = SpecifyAmount(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            return redirect(pay, amount=amount, transaction_type='C')
        else:
            HttpResponse('Form inputs are not valid')
    elif request.method == 'GET':  # the user should be directed to a page for specifying the amount
        form = SpecifyAmount()
        return render(request, 'financial_transaction/form_viewer.html', {'form': form})


# @login_required(login_url='sign_in')
def pay(request, amount, transaction_type):
    print('#################################################################')
    print(transaction_type)
    print('#################################################################')
    if request.method == 'POST':  # maybe we have to call bank api and output the result of transaction and the
        # transaction should be saved in db
        # if the transaction_type is C just charge the account
        # if the transaction_type is B then the charge of seller should be decreased
        # TODO
        return HttpResponse(amount)
    elif request.method == 'GET':  # the bank page should be represented and the card details have to be gotten
        form = BankForm()
        return render(request, 'financial_transaction/form_viewer.html', {'form': form})