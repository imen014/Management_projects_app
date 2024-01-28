from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from app_project.models import PermissionCreator, AttribuerPermission



class UserCreatorForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username','tel','email','role']


class Login_user_form(forms.Form):
    username=forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

class PermissionCreatorForm(forms.ModelForm):
    class Meta:
        model = PermissionCreator
        fields = ['codename','name','content_type']

class AttribuerPermissionForm(forms.ModelForm):
    class Meta:
        model = AttribuerPermission
        fields = ['permission','users']

    