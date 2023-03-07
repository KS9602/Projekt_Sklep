from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *


class RegistrationForm(UserCreationForm):
    class Meta:
        
        model = User
        fields = ['username','email','password1','password2']
    
class LoginForm(AuthenticationForm):
    class Meta:
        pass
    
class CreateProductForm(ModelForm):
    class Meta:
        
        model = Product
        fields = '__all__'
        widgets = { 'price': forms.NumberInput(attrs={'step': '0.01'}) }

class CreateAdvertisementForm(ModelForm):

    class Meta:

        model = Advertisement
        fields = '__all__'

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['products'] = forms.ModelMultipleChoiceField(
            queryset=user.shopuser.products.all(),
            widget=forms.SelectMultiple
        )


class EditUserProfile(ModelForm):
    class Meta:
        
        model = ShopUser
        fields = '__all__'
        exclude = ['user','username']
        widgets = {'address': forms.Textarea(attrs={'cols':40,'row':3,'style':'width:300px;height:100px'})}


class OrderForm(ModelForm):
    class Meta:

        model = Order
        fields = '__all__'
        widgets = {'total_price':forms.NumberInput(attrs={'readonly': 'readonly'}),
                   'buyer':forms.TextInput(attrs={'readonly': 'readonly'}),
                   'seller':forms.TextInput(attrs={'readonly': 'readonly'}),
                   'advertisement':forms.TextInput(attrs={'readonly': 'readonly'})}
        

