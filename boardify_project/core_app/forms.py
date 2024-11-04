from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate
from .models import Board,UserProfile

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label="Имя пользователя", max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя'}))
    first_name = forms.CharField(label="Имя", max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Введите имя'}))
    last_name = forms.CharField(label="Фамилия", max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Введите фамилию'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','password1','password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя", max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))

    class Meta:
        model=User
        fields=['username','password']

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'image', 'description', 'price', 'location', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Введите заголовок'}),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Введите описание'}),
            'price': forms.TextInput(attrs={'placeholder': 'Введите цену'}),
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'avatar', 'location']
        widgets = {
            'phone': forms.TextInput(attrs={'placeholder': '+77777777777'}),
        }
