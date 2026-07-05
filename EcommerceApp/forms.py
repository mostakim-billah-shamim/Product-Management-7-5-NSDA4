from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'user_type']


class AdminForm(forms.ModelForm):
    class Meta:
        model = AdminModel
        fields = '__all__'
        exclude = ['user']



class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerModel
        fields = '__all__'
        exclude = ['user']



class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = '__all__'
        


class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = '__all__'
        exclude = ['user']


