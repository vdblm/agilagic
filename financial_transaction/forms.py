from django import forms


class SpecifyAmount(forms.Form):
    amount = forms.IntegerField(min_value=0, max_value=1000000)


class BankForm(forms.Form):
    card_number = forms.IntegerField()
    cvv2 = forms.IntegerField()
    expiration_data = forms.IntegerField()
    second_password = forms.IntegerField()