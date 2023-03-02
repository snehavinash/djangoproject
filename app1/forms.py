from django import forms
from.models import SignUp,Gallery

class LoginForms(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    class Meta():
        model=SignUp
        fields=('Email','Password')
class UpdateForms(forms.ModelForm):
    class Meta():
        model=SignUp
        fields=('Name','Place','Email')
class ChangePasswordForms(forms.Form):
    Oldpassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    Newpassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    Confirmpassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    class Meta():
        model=SignUp
        fields=('Password')
class UpdateForms(forms.ModelForm):
    class Meta():
        model=SignUp
        fields=('Name','Place','Email')

class SignUpForms(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    Confirmpassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    class Meta():
        model=SignUp
        fields='__all__'

