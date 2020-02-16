from django import forms


class ProposeProduct(forms.Form):
    name = forms.CharField(max_length=50)
    available_number = forms.IntegerField()
    description = forms.CharField(max_length=200)
    price = forms.IntegerField()
    # TODO: a field for image should be created - then it should be implemented in the views

