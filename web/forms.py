from django import forms


class SignUpForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()


class SignInForm(forms.Form):
    email = forms.EmailField(required=True, initial='id@domain.com', max_length=20)
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8)
    # address = forms.CharField(widget=forms.Textarea)