from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField()
    username = forms.CharField(max_length=150, error_messages={'invalid':'Incorrect Username'})

    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2',]

