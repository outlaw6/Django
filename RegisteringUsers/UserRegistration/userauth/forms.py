from django import forms
from django.contrib.auth.models import User

from userauth.models import UserProfileInfo

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password') #these are the fields for the forms
                                                   # we wont take First and Last name fields

class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
