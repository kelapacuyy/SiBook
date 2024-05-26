from django import forms
from .models import Customer, Address
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.forms import ClearableFileInput

class UserRegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Masukkan username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Masukkan alamat email'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Masukkan kata sandi'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Masukkan ulang kata sandi'})
        self.fields['username'].label = 'Username'
        self.fields['email'].label = 'Email'
        self.fields['password1'].label = 'Kata Sandi'
        self.fields['password2'].label = 'Masukkan ulang kata sandi'
        self.fields['username'].help_text = None

    password1 = forms.CharField(widget=forms.PasswordInput, help_text='')
    password2 = forms.CharField(widget=forms.PasswordInput, help_text='')
    
    class Meta:
        model = Customer
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Masukkan username'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Masukkan kata sandi'})
        self.fields['username'].label = 'Username'
        self.fields['password'].label = 'Kata Sandi'

    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'label', 'receiver_name', 'receiver_phone', 'province', 'city', 'district', 'ward', 'zipcode', 'full_address'
        ]
        widgets = {
            'label': forms.TextInput(attrs={'placeholder': 'Rumah, Kos, dll'}),
            'receiver_name': forms.TextInput(attrs={'placeholder': 'Nama Penerima'}),
            'receiver_phone': forms.TextInput(attrs={'placeholder': 'No. HP Penerima'}),
            'province': forms.TextInput(attrs={'placeholder': 'Provinsi'}),
            'city': forms.TextInput(attrs={'placeholder': 'Kota'}),
            'district': forms.TextInput(attrs={'placeholder': 'Kecamatan'}),
            'ward': forms.TextInput(attrs={'placeholder': 'Kelurahan'}),
            'zipcode': forms.TextInput(attrs={'placeholder': 'Kode Pos'}),
            'full_address': forms.Textarea(attrs={'placeholder': 'Alamat lengkap', 'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False
            field.label = False

class ProfilePictureForm(forms.ModelForm):
    profile_picture = forms.ImageField(
        label=None,
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control-file'})
    )

    class Meta:
        model = Customer
        fields = ['profile_picture']

class CustomPasswordChangeForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs['placeholder'] = 'Masukkan kata sandi lama'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'Masukkan kata sandi baru'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Masukkan ulang kata sandi baru'
        self.fields['old_password'].label = 'Password lama:'
        self.fields['new_password1'].label = 'Password baru:'
        self.fields['new_password2'].label = 'Masukkan ulang password baru:'

    old_password = forms.CharField(widget=forms.PasswordInput, help_text='')
    new_password1 = forms.CharField(widget=forms.PasswordInput, help_text='')
    new_password2 = forms.CharField(widget=forms.PasswordInput, help_text='')
