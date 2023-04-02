from django import forms
from django.contrib.auth.models import AbstractUser

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegForm(forms.Form):
    username = forms.CharField()
    mail = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)

class UserInfoForm(forms.Form):
    first_name = forms.CharField()
    middle_name = forms.CharField()
    last_name = forms.CharField()
    mail = forms.CharField()
    job = forms.CharField()
    birth_date = forms.DateField()

class TeamForm(forms.Form):
    team = forms.CharField()
    name = forms.CharField()
class TeamMemberForm(forms.Form):
    name = forms.CharField()

MemberFormset = forms.formset_factory(TeamMemberForm, extra=1)