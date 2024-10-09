from django import forms
from django.forms import ModelForm
from .models import Product
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product  # Link to your Product model
        fields = ['album_title', 'artist_name', 'price', 'description']  # Specify the fields

    # Clean and sanitize album_title
    def clean_album_title(self):
        album_title = self.cleaned_data.get("album_title")
        # Strip any HTML tags for security reasons
        cleaned_album_title = strip_tags(album_title)
        return cleaned_album_title

    # Clean and sanitize artist_name
    def clean_artist_name(self):
        artist_name = self.cleaned_data.get("artist_name")
        # Strip any HTML tags for security reasons
        cleaned_artist_name = strip_tags(artist_name)
        return cleaned_artist_name

    # Clean and sanitize description
    def clean_description(self):
        description = self.cleaned_data.get("description")
        # Strip any HTML tags for security reasons
        cleaned_description = strip_tags(description)
        return cleaned_description

    # Optionally, you can also validate price if needed
    def clean_price(self):
        price = self.cleaned_data.get("price")
        # Example validation: price should be a positive number
        if price < 0:
            raise forms.ValidationError("Price cannot be negative.")
        return price

        
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