from django import forms 
from first_app.models import User,UserProfileInfo

class FormName(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ['profile_site','profile_pic']

