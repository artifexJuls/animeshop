from django import forms
from .models import Clothes, Registration, UserProfile, Order


class ClothesForm(forms.ModelForm):
    class Meta:
        model = Clothes
        fields = '__all__'


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['nickname', 'email', 'phone', 'password']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user', 'password']

    avatar = forms.ImageField(required=False, widget=forms.FileInput)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user_profile', 'total_price', 'product_amount', 'is_completed', 'address', 'item_names']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_profile'].required = False

