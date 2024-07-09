from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

from django import forms
from django.forms.widgets import PasswordInput, TextInput

# Create/register a user (Model form)
class SignUpForm(UserCreationForm):
  class Meta:
    model = User
    fields = ('email', 'name', 'password1', 'password2')

# Authenticate a user (Model form)
class LoginForm(AuthenticationForm):
  username = forms.CharField(widget=TextInput())
  password = forms.CharField(widget=PasswordInput())
  