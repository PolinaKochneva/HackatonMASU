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

class HackathonForm(forms.Form):
    name = forms.CharField()
    start_date = forms.DateField()
    end_date = forms.DateField()
    description = forms.CharField()

class HackathonDateForm(forms.Form):
    start_date = forms.DateField()
    end_date = forms.DateField()

MemberFormset = forms.formset_factory(TeamMemberForm, extra=1)