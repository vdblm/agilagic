from django import forms


class SignUpForm(forms.Form):
    name = forms.CharField()


class SignInForm(forms.Form):
    name = forms.CharField()
    password = forms.CharField()
    email = forms.EmailField()
