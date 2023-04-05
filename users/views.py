from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.forms import formset_factory
from .forms import LoginForm, RegForm, UserInfoForm, TeamForm, TeamMemberForm, MemberFormset
from .models import Teams, MemberTeam, Profile, Tasks

# Create your views here.
def profile(request):
    if not User.objects.filter(username=request.user.username):
        context = 'пользователь не существует'
    else:
        context = 'пользователь существует'
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    return render(request, "users/personal.html", {

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
                return  HttpResponseRedirect(reverse('users:profile'))
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
    teams = Teams.objects.all()
    member_form = MemberFormset()
    return render(request, "users/add_command.html", {
        'teams': teams,
        'formset':member_form
    })

def del_command(request):
    team = Teams.objects.filter(name=request.user.memberteam.team)
    team.delete()
    return HttpResponseRedirect(reverse("users:command"))

def add_member(request):
    member_form = TeamMemberForm(request.POST)
    members = member_form.data.getlist('name')
    users = User.objects.filter(username__in=members)
    for user in users:
        team_member = MemberTeam(team=request.user.memberteam.team, user=user)
        team_member.save()
    return HttpResponseRedirect(reverse("users:command"))

def del_member(request):
    member_form = TeamMemberForm(request.POST)
    members = member_form.data.getlist('name')
    users = User.objects.filter(username__in=members)
    for user in users:
        user.memberteam.delete()
    return HttpResponseRedirect(reverse("users:command"))
def command(request):
# Должна быть проверка на существование команды в БД -- ГОТОВО
# Если существует, то запрет на создание -- ГОТОВО
# Если не существует, то проверка есть ли у предлагаемых участников команда -- ГОТОВО
# Если все участники свободны, то создание команды и привязка участников к команде -- ГОТОВО
# Если участник уже в команде, то вывод страницы с инфой о команде и настройками (в html можно настроить)
# Проблема: Нужна таблица с командами, расширить модель User, обработка формы разных размеров -- ГОТОВО
    if MemberTeam.objects.filter(user=request.user):
        return render(request, "users/team.html", {'members':request.user.memberteam.team_members(team=request.user.memberteam.team)})
    else:

        if request.method == 'POST':
            team_form = TeamForm(request.POST)
            if team_form.is_valid():
                team_name = team_form.cleaned_data['team']
                members = team_form.data.getlist('name')
                users = User.objects.filter(username__in=members)
                if (not Teams.objects.filter(name=team_name)) \
                        and (users.count() == int(request.POST['form-TOTAL_FORMS']))\
                        and not all(MemberTeam.objects.filter(user=user) for user in users):
                    team = Teams(name=team_name)
                    team.save()
                    for user in users:
                        team_member = MemberTeam(team=team, user=user)
                        team_member.save()
                    team_member = MemberTeam(team=team, user=request.user)
                    team_member.save()
                    return render(request, "users/team.html",
                                  {'members': request.user.memberteam.team_members(team=request.user.memberteam.team)})

                else:
                    return render(request, "users/personal.html", {
                        'message':'Команда уже существует, либо пользователей которых вы пытаетесь добавить не существует, либо уже заняты в другой команде',
                    })

                return HttpResponseRedirect(reverse("users:add_command"))
            else:

                return render(request, "users/personal.html", {

                    'message': 'форма/не/валидна',
                })
        else:
            return HttpResponseRedirect(reverse("users:profile"))
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
                    return HttpResponseRedirect(reverse('users:profile'))

            else:
                return render(request, "users/registration.html", {
                    'message': 'Пользователь существует',
                })

    return render(request, "users/registration.html", {
        'message':'Invalid form',
    })



def update_user_info(request):
    if request.method == 'POST' and request.user.is_authenticated:

        form = UserInfoForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data

            # Обернуть этот блок в try/except
            user = User.objects.get(username=request.user.username)

            if not Profile.objects.filter(user=request.user):
                profile = Profile(user=request.user,
                                  middle_name=cd['middle_name'],
                                  job=cd['job'],
                                  birth_date=cd['birth_date'],)
                user.first_name = cd['first_name']
                user.last_name = cd['last_name']
                if user.email != cd['mail']:
                    user.email = cd['mail']
                profile.save()
                user.save()

            else:
                if user.first_name != cd['first_name']:
                    user.first_name = cd['first_name']

                if user.profile.middle_name != cd['middle_name']:
                    user.profile.middle_name = cd['middle_name']

                if user.last_name != cd['last_name']:
                    user.last_name = cd['last_name']

                if user.email != cd['mail']:
                    user.email = cd['mail']

                if user.profile.job != cd['job']:
                    user.profile.job = cd['job']

                if user.profile.birth_date != cd['birth_date']:
                    user.profile.birth_date = cd['birth_date']

                user.save()
                user.profile.save()

            # Сделать вывод сообщения об изменении данных
            return HttpResponseRedirect(reverse("users:profile"))
        else:
            return render(request, "users/personal.html", {

                'message': 'Неправильно заполненная форма',
            })
    else:
        return HttpResponseRedirect(reverse("users:profile"))

def delete_user(request):
    user = User.objects.get(username=request.user.username)
    User.delete(user)
    logout(request)
    return render(request, 'users/login.html', {
        'message': 'Вы вышли из системы',
    })

def schedule(request):
    return render(request, 'users/schedule.html',)

def task(request):
    if request.user.memberteam.team.task_id:
        return render(request, 'users/user_task.html', {
            'link':request.user.memberteam.team.task_id.link_to_the_task_text
        })
    else:
        return render(request, 'users/tasks.html', )

def new_task(request):
    team = request.user.memberteam.team
    task = Tasks.objects.get(link_to_the_task_text=request.POST['link'])
    team.task_id = task
    team.save()
    return HttpResponseRedirect(reverse('users:task'))

def change_task(request):
    team = request.user.memberteam.team
    team.task_id = None
    team.save()
    return HttpResponseRedirect(reverse('users:task'))