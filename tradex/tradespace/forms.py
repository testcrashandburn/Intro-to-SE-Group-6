from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Product
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = CustomUser
        fields = ("username", "email","user_type")
        def clean_email(self):
            email = self.cleaned_data.get('email')
            if not email:
                raise forms.ValidationError("Email field is required")
            return email

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email","user_type")





class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'digital', 'image']
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ProductForm, self).__init__(*args, **kwargs)
        if self.user:
            self.instance.creator = self.user