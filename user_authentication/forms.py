from django import  forms


class SignInForm(forms.Form):
    email = forms.EmailField(required=True, initial='id@domain.com', max_length=20, label='ایمیل')
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8, label='رمز عبور')
    # address = forms.CharField(widget=forms.Textarea)


class CustomerSignUpForm(forms.Form):
    email = forms.EmailField(initial='id@domain.com', required=True, label='ایمیل')
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8, required=True, label='رمز ورود')
    name = forms.CharField(required=True, label='نام')
    family_name = forms.CharField(required=True, label='نام خانوادگی')


class SellerSignUpForm(forms.Form):
    email = forms.EmailField(initial='id@domain.com', required=True, label='ایمیل')
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8, required=True, label='رمز ورود')
    name = forms.CharField(required=True, label='نام شرکت')
    number = forms.IntegerField(required=True, label='شماره شرکت')
