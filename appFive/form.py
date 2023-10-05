from django import forms 
from appFive.models import UserInfoApp,UserProfileInfoApp

class UserInfoAppForm(forms.ModelForm):
    class Meta:
        model = UserInfoApp
        fields = ['user','email','password']

class UserProfileFormAppForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfoApp
        fields = ['profile_site_app','profile_pic_app']

