from django import forms
from app.models import Register,task

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model=Register
        fields='__all__'

class Userdata(forms.ModelForm):
    class Meta:
        model=task
        fields='__all__'