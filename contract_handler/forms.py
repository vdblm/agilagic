from django import forms


class ProposeContract(forms.Form):
    percentage = forms.IntegerField(
        required=True,
        label='درصد سود دارنده‌ی سایت',
        error_messages={'required': 'لطفا درصد تقسیم سود را وارد کنید'},
        min_value=0,
        max_value=100
    )
    description = forms.CharField(
        widget=forms.Textarea,
        label='توضیحات',
        required=True,
        error_messages={'required': 'لطفا توضیحاتی برای قرارداد بنویسید'}
    )

    # TODO: a field for image should be created - then it should be implemented in the views
