from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegForm(forms.Form):
    username = forms.CharField()
    mail = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)