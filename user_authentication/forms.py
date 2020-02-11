from django import forms


class SignInForm(forms.Form):
    email = forms.EmailField(
        required=True,
        initial='id@domain.com',
        label='ایمیل',
        error_messages={'required': 'لطفا ایمیل خود را وارد کنید',
                        'invalid': 'فرمت ایمیل اشتباه است'},
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        min_length=8,
        required=True,
        label='رمز عبور',
        error_messages={'min_length': 'رمز عبور انتخابی باید حداقل ۸ کاراکتر باشد',
                        'required': 'لطفا رمز عبور را وارد کنید'}
    )


class CustomerSignUpForm(SignInForm):
    name = forms.CharField(
        required=True,
        label='نام',
        error_messages={'required': 'لطفا نام خود را وارد کنید'}
    )
    family_name = forms.CharField(
        required=True,
        label='نام خانوادگی',
        error_messages={'required': 'لطفا نام خانوادگی خود را وارد کنید'}
    )


class SellerSignUpForm(SignInForm):
    name = forms.CharField(
        required=True,
        label='نام شرکت',
        error_messages={'required': 'لطفا نام شرکت را وارد کنید'}
    )
    number = forms.IntegerField(
        required=True,
        label='شماره شرکت',
        error_messages={'required': 'لطفا شماره شرکت را وارد کنید'}
    )
