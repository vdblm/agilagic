from django.shortcuts import render
from .forms import ProposeContract
from .models import Contract
from user_authentication.models import UserManager
# Create your views here.


def propose_contract(request):  # the proposed contract should be made and added to the database
    if request.method == 'POST':
        propose_contract = ProposeContract(request.POST)
        if propose_contract.is_valid():
            description = propose_contract.cleaned_data['description']
            percentage = propose_contract.cleaned_data['percentage']
            seller = UserManager.get_seller_by_username(request.user.username)
            contract = Contract(description=description, percentage=percentage, status='P', seller=seller)
            contract.save()
        else:
            pass
        return 'vahid_handler'