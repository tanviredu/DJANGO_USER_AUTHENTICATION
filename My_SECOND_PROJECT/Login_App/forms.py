from django import forms
from django.contrib.auth.models import User
from .models import UserInfo


class UserForm(forms.ModelForm):
    
    ## override the password field
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        ## using three field
        fields = ('username','email','password')

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('facebook','profile_pic')



