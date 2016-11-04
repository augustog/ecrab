from django import forms
from django.contrib.auth.models import Usuario
from django.forms import ModelForm
 
 
class SignUpForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password', 'name', 'lastname']
        widgets = {
            'password': forms.PasswordInput(),
        }