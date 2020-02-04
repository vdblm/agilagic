from django import forms


class SignInForm(forms.Form):
    email = forms.EmailField(required=True, initial='id@domain.com', max_length=20)
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8)
    # address = forms.CharField(widget=forms.Textarea)


class SignUpForm(forms.Form):
    email = forms.EmailField(initial='id@domain.com', required=True)
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8, required=True)
    name = forms.CharField(required=True)
    family_name = forms.CharField(required=True, label='Family Name')
    type = forms.MultipleChoiceField(label='Join as a seller', widget=forms.CheckboxInput(), required=False)


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
