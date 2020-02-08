from django import forms


class SignInForm(forms.Form):
    email = forms.EmailField(required=True, initial='id@domain.com', max_length=20, label='ایمیل')
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8, label='رمز عبور')
    # address = forms.CharField(widget=forms.Textarea)


class SignUpForm(forms.Form):
    email = forms.EmailField(initial='id@domain.com', required=True, label='ایمیل')
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8, required=True, label='رمز ورود')
    name = forms.CharField(required=True, label='نام')
    family_name = forms.CharField(required=True, label='نام خانوادگی')
    type = forms.MultipleChoiceField(label='ثبت‌نام به عنوان فروشنده', widget=forms.CheckboxInput(), required=False)


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
