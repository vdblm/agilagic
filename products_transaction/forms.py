from django import forms


class ProposeProduct(forms.Form):
    name = forms.CharField(
        max_length=50,
        required=True,
        label='نام کالا',
        error_messages={'required': 'لطفا نام کالا را وارد کنید'}
    )
    available_number = forms.IntegerField(
        required=True,
        label='تعداد موجودی',
        error_messages={'required': 'لطفا تعداد موجودی را وارد کنید'}
    )
    description = forms.CharField(
        widget=forms.Textarea,
        label='توضیحات',
        required=True,
        error_messages={'required': 'لطفا توضیحاتی برای کالا بنویسید'}
    )
    price = forms.IntegerField(
        label='قیمت کالا',
        required=True,
        error_messages={'required': 'لطفا قیمت کالا را وارد کنید'}
    )
    image = forms.ImageField(
        label='تصویر کالا',
        required=True,
        error_messages={'required': 'لطفا تصویر کالا را آپلود کنید'}
    )
    # TODO: a field for image should be created - then it should be implemented in the views
