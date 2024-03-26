from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
  username = forms.CharField(
    label="Username",
    widget=forms.TextInput(attrs={'class': 'form-input'})
  )
  password = forms.CharField(
    label="Password",
    widget=forms.PasswordInput(attrs={'class': 'form-input'})
  )

class UserForm(UserCreationForm):

  class Meta:
    model = User
    fields = ('username', 'password1', 'password2')
    widgets = {
      'username': forms.TextInput(attrs={'class': 'form-input'}),
      'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
      'passowrd2': forms.PasswordInput(attrs={'class': 'form-input'}),
    }