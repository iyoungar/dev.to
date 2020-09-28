from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models

class CreateUserForm (UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'space', 'placeholder': 'username '}),
            'email': forms.EmailInput(attrs={'class': 'space', 'placeholder': 'email'}),
            'password1': forms.PasswordInput(attrs={'class': 'space',}),
            'password2': forms.PasswordInput(attrs={'class': 'space',}),
        }