from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@login_required(login_url='sign_in')
@csrf_exempt
def charge_account(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        pass


@login_required(login_url='sign_in')
def pay_for_product(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        pass