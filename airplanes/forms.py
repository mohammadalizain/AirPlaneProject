from django import forms
from .models import airplanes

class airplanesForm(forms.ModelForm):
    class Meta:
        model = airplanes
        fields=['name','weight','passengers','other_info','picture']