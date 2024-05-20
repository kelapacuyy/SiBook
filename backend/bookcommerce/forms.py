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
        self.fields['username'].label = 'Username:'
        self.fields['email'].label = 'Email:'
        self.fields['password1'].label = 'Password:'
        self.fields['password2'].label = 'Masukkan ulang password:'
        self.fields['username'].help_text = None
    
    password1 = forms.CharField(widget=forms.PasswordInput, help_text='')
    password2 = forms.CharField(widget=forms.PasswordInput, help_text='')
    
    class Meta:
        model = Customer
        fields = ['username', 'email', 'password1', 'password2']
