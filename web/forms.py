from django import forms


class ProposeContract(forms.Form):
    percentage = forms.IntegerField(min_value=0, max_value=100)
    description = forms.CharField(widget=forms.Textarea)


class ProposeProduct(forms.Form):
    name = forms.CharField(max_length=20)
    price = forms.IntegerField()
    description = forms.CharField(widget=forms.Textarea)
    img = forms.ImageField()


class ChargeAccount(forms.Form):
    amount = forms.IntegerField()
