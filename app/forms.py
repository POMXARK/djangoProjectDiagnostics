from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Login"}))
    password = forms.CharField(label='',
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Password"}))
