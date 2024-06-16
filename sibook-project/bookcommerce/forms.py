from django import forms
from .models import Customer, Address, Review
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
            'label': forms.TextInput(attrs={'placeholder': 'Rumah, Kos, dll', 'class': 'custom-placeholder'}),
            'receiver_name': forms.TextInput(attrs={'placeholder': 'Nama Penerima', 'class': 'custom-placeholder'}),
            'receiver_phone': forms.NumberInput(attrs={'placeholder': 'No. HP Penerima', 'class': 'custom-placeholder'}),
            'province': forms.TextInput(attrs={'placeholder': 'Provinsi', 'class': 'custom-placeholder'}),
            'city': forms.TextInput(attrs={'placeholder': 'Kota', 'class': 'custom-placeholder'}),
            'district': forms.TextInput(attrs={'placeholder': 'Kecamatan', 'class': 'custom-placeholder'}),
            'ward': forms.TextInput(attrs={'placeholder': 'Kelurahan', 'class': 'custom-placeholder'}),
            'zipcode': forms.NumberInput(attrs={'placeholder': 'Kode Pos', 'class': 'custom-placeholder'}),
            'full_address': forms.Textarea(attrs={'placeholder': 'Alamat lengkap', 'rows': 3, 'class': 'custom-placeholder'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False
            field.label = False

        self.fields['receiver_name'].required = True
        self.fields['receiver_phone'].required = True
        self.fields['province'].required = True
        self.fields['city'].required = True
        self.fields['district'].required = True
        self.fields['zipcode'].required = True
        self.fields['full_address'].required = True

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

    def clean(self):
        cleaned_data = super().clean()
        old_password = cleaned_data.get('old_password')
        new_password1 = cleaned_data.get('new_password1')
        
        if old_password and new_password1 and old_password == new_password1:
            raise forms.ValidationError('Password baru tidak boleh sama dengan password lama.')
        
        return cleaned_data

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'content']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5, 'step': 1, 'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Tulis ulasan di sini...'}),
        }
