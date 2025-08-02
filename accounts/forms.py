from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.Form):
    first_name = forms.CharField(
        max_length=30, 
        required=True, 
        widget=forms.TextInput()
    )
    last_name = forms.CharField(
        max_length=30, 
        required=True, 
        widget=forms.TextInput()
    )
    username = forms.CharField(
        max_length=150, 
        required=True, 
        widget=forms.TextInput()
    )
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput()
    )
    password = forms.CharField(
        required=True, 
        widget=forms.PasswordInput()
    )
    account_type = forms.ChoiceField(
        choices=(
            ('customer', 'Customer - Browse and buy products'),
            ('seller', 'Seller - List and sell products'),
        ),
        required=True,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already taken. Please choose another one.")
        return username
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already registered. Please use a different email.")
        return email