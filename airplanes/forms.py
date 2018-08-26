from django import forms
from .models import airplanes
from django.contrib.auth.models import User


class airplanesForm(forms.ModelForm):
    class Meta:
        model = airplanes
        fields=['name','weight','passengers','other_info','picture']




class UserLogin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())



class UserRegister(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email' ,'password']

        widgets={
        'password': forms.PasswordInput(),
        }