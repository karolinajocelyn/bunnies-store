from django import forms
from django.forms import ModelForm
from .models import Product
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class ProductForm(ModelForm):
    class Meta:
        model = Product  # This is the model the form is based on
        fields = ['artist_name', 'album_title', 'price', 'description']  # Include the fields you want to display in the form

        # Optional: Customize widgets for form fields
        widgets = {
            'artist_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the artist name',
            }),
            'album_title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the album title',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the price',
                'min': 0
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the album description',
                'rows': 3,
            }),
        }
        
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full max-w-lg px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-pink-500 focus:border-pink-500 text-center',
        'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full max-w-lg px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-pink-500 focus:border-pink-500 text-center',
        'placeholder': 'Password'
    }))

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        
        # Define widgets with custom classes
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full max-w-lg px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-pink-500 focus:border-pink-500 text-center',
                'placeholder': 'Username'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'w-full max-w-lg px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-pink-500 focus:border-pink-500 text-center',
                'placeholder': 'Password'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'w-full max-w-lg px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-pink-500 focus:border-pink-500 text-center',
                'placeholder': 'Password confirmation'
            }),
        }