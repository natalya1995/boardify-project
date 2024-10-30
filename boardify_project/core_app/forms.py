from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate
from .models import Board,UserProfile

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','password1','password2']


class UserLoginForm(AuthenticationForm):
    class Meta:
        model=User
        fields=['username','password']

class BoardForm(forms.ModelForm):
    class Meta:
        model=Board
        fields=['title','image','description','price','location','category']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['phone','avatar','location']