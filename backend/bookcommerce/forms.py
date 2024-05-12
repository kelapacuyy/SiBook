from django import forms
from .models import Customer
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Masukkan username'
        self.fields['email'].widget.attrs['placeholder'] = 'Masukkan alamat email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Masukkan password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Masukkan ulang password'
        self.fields['username'].label = False
        self.fields['email'].label = False
        self.fields['password1'].label = False
        self.fields['password2'].label = False
    
    password1 = forms.CharField(widget=forms.PasswordInput, help_text='')
    password2 = forms.CharField(widget=forms.PasswordInput, help_text='')
    
    class Meta:
        model = Customer
        fields = ['username', 'email', 'password1', 'password2']
