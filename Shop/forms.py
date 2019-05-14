from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegister(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Please enter a valid mail address.")
    firstname = forms.CharField(max_length="30", required=True)
    lastname = forms.CharField(max_length="30", required=True)
    phone =  forms.IntegerField(required=True)

    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'username', 'email',  'phone', 'password1', 'password2']