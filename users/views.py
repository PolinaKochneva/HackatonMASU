from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import LoginForm, RegForm

# Create your views here.
def index(request):
    if not User.objects.filter(username=request.user.username):
        context = 'пользователь не существует'
    else:
        context = 'пользователь существует'
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    return render(request, "users/profile.html", {

        'message':context,
    })

def login_view(request):
    if request.method == 'POST':

        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user is not None:
                login(request, user)
                return  HttpResponseRedirect(reverse('users:index'))
            else:
                return render(request, 'users/login.html', {
                    'message':'Неправильное имя пользователя или пароль',
                })

    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, 'users/login.html', {
        'message': 'Вы вышли из системы',
    })

def add_command(request):
    return render(request, "users/add_command.html")

def register(request):

    if request.method == 'POST':

        form = RegForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            if (not User.objects.filter(username=cd['username'])) and (not User.objects.filter(email=cd['mail'])) :
                User.objects.create_user(username=cd['username'], email=cd['mail'], password=cd['password'])
                user = authenticate(username=cd['username'], password=cd['password'])

                if user is not None:
                    login(request, user)
                    return render(request, "users/profile.html", {
                    })
            else:
                return render(request, "hackaton/registration.html", {
                    'message': 'Пользователь существует',
                })

    return render(request, "hackaton/registration.html", {
        'message':'Invalid form',
    })