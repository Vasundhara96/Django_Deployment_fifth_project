from django import forms
from usermodel_app.models import UserProfInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfInfo
        exclude = ('user',)
