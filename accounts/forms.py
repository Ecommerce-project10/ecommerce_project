from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from accounts.models import Create_USER 

class UserRegistrationForm(ModelForm):
    account_type = forms.ChoiceField(choices=Create_USER.ACCOUNT_TYPES,
                                     required= True,
                                     widget=forms.TextInput
                                     )
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {
            'password': forms.PasswordInput(),
        }
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            Create_USER.objects.create(user=user, account_type=self.cleaned_data['account_type'])
        return user
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